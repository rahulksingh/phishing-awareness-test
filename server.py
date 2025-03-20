from flask import Flask, request
import os

# Ensure the file exists
FILE_PATH = "clicked_users.txt"
if not os.path.exists(FILE_PATH):
    open(FILE_PATH, "w").close()

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_email():
    data = request.json
    with open(FILE_PATH, "a") as file:
        file.write(data['email'] + "\n")
    return "Logged", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
