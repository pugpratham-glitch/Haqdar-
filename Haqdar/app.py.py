from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    # Try reading index.html directly from root or templates
    paths_to_check = ["index.html", "templates/index.html", "Haqdar/index.html"]
    for path in paths_to_check:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    return "Error: index.html not found in repository structure.", 404

@app.route("/api/match", methods=['GET'])
def match_opportunities():
    age = request.args.get("age", "0")
    income = request.args.get("income", "0")
    state = request.args.get("state", "All India")
    category = request.args.get("category", "General")

    mock_database = [
        {
            "id": "nat-001",
            "title": {
                "en": "National Scholarship Portal (NSP) Central Sector Scheme",
                "hi": "राष्ट्रीय छात्रवृत्ति पोर्टल केंद्रीय क्षेत्र योजना"
            },
            "domicile": "All India",
            "type": "Scholarship",
            "official_link": "https://scholarships.gov.in/"
        },
        {
            "id": "nat-002",
            "title": {
                "en": "UPSC Civil Services Examination Fee Exemption & Coaching Support",
                "hi": "यूपीएससी सिविल सेवा परीक्षा शुल्क छूट और कोचिंग सहायता"
            },
            "domicile": "All India",
            "type": "Competitive Exam",
            "official_link": "https://upsc.gov.in/"
        },
        {
            "id": "mah-001",
            "title": {
                "en": "Maharashtra Post-Matric Scholarship for Backward Class Students",
                "hi": "महाराष्ट्र पिछड़ा वर्ग छात्रों के लिए पोस्ट-मैट्रिक छात्रवृत्ति"
            },
            "domicile": "Maharashtra",
            "type": "Scholarship",
            "official_link": "https://mahadbtmahadbt.gov.in/"
        }
    ]

    filtered = [
        item for item in mock_database 
        if item["domicile"] == state or item["domicile"] == "All India"
    ]

    return jsonify({
        "success": True,
        "count": len(filtered),
        "matches": filtered,
        "received_params": {
            "age": age,
            "income": income,
            "state": state,
            "category": category
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
