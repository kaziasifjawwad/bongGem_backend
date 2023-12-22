from flask import Flask, render_template, request, jsonify

from inference.textgenerator import generate_text

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    response = generate_text(user_message)
    return jsonify({'message': response})


if __name__ == '__main__':
    app.run(debug=True)
