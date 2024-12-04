from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    data = request.get_json()
    length = data.get('length')
    include_special = data.get('specialChars', False)

    # Validate length
    if not length or length <= 0:
        return jsonify({"error": "Invalid length"}), 400

    # Password characters
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
