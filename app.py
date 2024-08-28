from flask import Flask, request, jsonify,render_template,url_for
import os

app = Flask(__name__)

messages = []

# GET route for basic testing
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        # Store user message
        messages.append({'role': 'user', 'message': user_message})

        import google.generativeai as genai
        genai.configure(api_key=os.environ['API_KEY'])
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Generate response from the model
        response = model.generate_content(user_message)

        # Store bot response
        messages.append({'role': 'bot', 'message': response.text})

        return jsonify({"reply": response.text, "messages": messages})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)