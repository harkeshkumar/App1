from flask import Flask, request, jsonify
from utilities import Utility

app = Flask(__name__)


@app.route("/api", methods=["POST"])
def reverseString():
	data = request.get_json()
	return jsonify(message = Utility.getReverseString(data.get("message")), rand = Utility.getRandomNumber())

if __name__ == '__main__':
    app.run(debug=True)
