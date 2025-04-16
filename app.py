from flask import Flask, request, jsonify
from flask_cors import CORS  # Allow frontend to call backend
from chat import get_response  # Import chatbot function

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route('/')
def home():
    return "Chatbot API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debugging line
        
        # Check if message exists
        if not data or "message" not in data:
            return jsonify({"answer": "Invalid request, please send a message."}), 400
        
        user_message = data["message"]

        # Get chatbot response
        bot_response = get_response(user_message)

        print("Sending response:", bot_response)  # Debugging line
        return jsonify({"answer": bot_response})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"answer": "An error occurred on the server."}), 500

if __name__ == '__main__':
    app.run(debug=True)
