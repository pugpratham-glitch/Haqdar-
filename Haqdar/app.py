from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    # Serves the actual visual frontend interface
    return render_template("index.html")

@app.route("/api/match", methods=['GET'])
def match_opportunities():
    age = request.args.get("age", "0")
    income = request.args.get("income", "0")
    state = request.args.get("state", "All India")
    category = request.args.get("category", "General")

    mock_database = [
        {
            "id": "mah-001",
            "title": "Post-Matric Scholarship Scheme for SC Students",
            "domicile": "Maharashtra",
            "type": "Scholarship",
            "official_link": "https://mahadbtmahadbt.gov.in/"
        }
    ]

    return jsonify({
        "success": True,
        "count": len(mock_database),
        "matches": mock_database,
        "received_params": {
            "age": age,
            "income": income,
            "state": state,
            "category": category
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
