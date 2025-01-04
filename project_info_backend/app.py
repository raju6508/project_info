from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

@app.route("/api/projects", methods=["GET"])
def get_project_info():
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",         # Change to your MySQL server host
            user="root",     # Replace with your MySQL username
            password="Raj6508$", # Replace with your MySQL password
            database="my_database"    # Replace with your database name
        )

        cursor = connection.cursor()
        query = "SELECT * FROM project_info;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        projects = [
            {"ID": row[0], "Project_Title": row[1], "PartNumbers": row[2], "Proj_Status": row[3], "Action": row[4]}
            for row in rows
        ]

        return jsonify(projects)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
