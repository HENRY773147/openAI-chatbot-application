from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if user_message.lower() == 'bye':
        return jsonify({'response': 'Bye'})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=50,
            n=1,
            temperature=0.3,
            messages=[{"role": "user", "content": user_message}]
        )
        assistant_response = response.choices[0].message.content
        return jsonify({'response': assistant_response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    import sys
print(sys.path)