from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from narrative import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kitandkaboodle'

try: 
    class TextInputForm(FlaskForm):
        text_input = StringField('What do you do?')
        submit = SubmitField('Send action')

    # Check if rag output filename exists in /assets

    def file_exists(filename):
        filepath = os.path.join(app.root_path, 'static', 'assets', filename)
        file_exists = os.path.isfile(filepath)
        # print(f"Checking if file exists: {filepath} - {file_exists}")  # Debugging statement
        return file_exists
        

    # Create a route to handle form submission

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = TextInputForm()
        background_image = '1.png'
        if form.validate_on_submit():
            # Get input text from the form
            user_input = form.text_input.data
            
            # Invoke storytelling_runnable to generate response

            response = storytelling_runnable.invoke(
            {"input": user_input, "IP": system_params["IP"], "rules": system_params["rules"], "injection_rules": system_params["injection_rules"]},
            config={"configurable": {"session_id": "abc123"}}
            )

            description = response.content

            # Pass output to RAG Chain

            rag_response = rag_chain.invoke(f"Return the most relevant filename based on the following story update. Prioritize key visual elements like roads, buildings, and environments. Return filename only: ' {user_input}. {description} ' ")

            # Update app background with RAG Chain output (you need to define this part)
            # For now, let's just print the RAG Chain output
            print(description, rag_response)

            # Check chat history if needed
            # chat_history = get_session_history(session_id)

            # for message in chat_history.messages:
            #     if isinstance(message, AIMessage):
            #         prefix = "AI"
            #     else:
            #         prefix = "User"
            #     print(f"{prefix}: {message.content}")
            
            # Check if the file exists in /assets directorypy
            if file_exists(rag_response):
                print("file checker working")
                background_image = rag_response
            
            #Update background image and display response
            return render_template('index.html', form=form, response=[description, rag_response], background_image=background_image)
        
        #Render
        return render_template('index.html', form=form, background_image=background_image)
except Exception as e:
    app.logger.error(f"Error during app startup: {e}")

if __name__ == '__main__':
    app.run(debug=True)
