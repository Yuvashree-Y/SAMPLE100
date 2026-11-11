from flask import Flask, request, jsonify

# 1. Initialize the Flask application first
app = Flask(__name__)

# 2. Define your routes using the initialized app
@app.route('/n8n-webhook', methods=['POST'])
def n8n_webhook():
    data = request.get_json()
    print("Received from n8n:", data)
    
    # Fixed the typo in "received" just in case!
    return jsonify({"status": "received", "data": data})

# 3. Add spaces around the conditional check to run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
