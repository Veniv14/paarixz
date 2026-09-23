from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# -------------------------------
# CONNECT TO MYSQL IN DOCKER
# -------------------------------
db = mysql.connector.connect(
    host="mysql-service",    # Name of the kubernetes service name that runs mysql
    user="root",
    password="password",
    database="contactsdb"
)
cursor = db.cursor()

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    sql = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, message))
    db.commit()

    return jsonify({"status": "success", "message": "Saved to DB"}), 200


@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
