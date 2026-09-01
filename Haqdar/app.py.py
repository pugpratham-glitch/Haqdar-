from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/api/match", methods=['GET'])
def match_opportunities():
    age = request.args.get("age", "0")
    income = request.args.get("income", "0")
    state = request.args.get("state", "All India")
    category = request.args.get("category", "General")

    # Comprehensive All-India Mock Database (Scholarships, Exams, and Welfare)
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
            "id": "nat-003",
            "title": {
                "en": "PM Young Achievers Scholarship Award Scheme for Vibrant India (YASASVI)",
                "hi": "पीएम युवा अचीवर्स छात्रवृत्ति योजना (YASASVI)"
            },
            "domicile": "All India",
            "type": "Scholarship",
            "official_link": "https://socialjustice.gov.in/"
        },
        {
            "id": "nat-004",
            "title": {
                "en": "AICTE Pragati Scholarship for Girl Students in Technical Education",
                "hi": "तकनीकी शिक्षा में छात्राओं के लिए एआईसीटीई प्रगति छात्रवृत्ति"
            },
            "domicile": "All India",
            "type": "Scholarship",
            "official_link": "https://www.aicte-india.org/"
        },
        {
            "id": "nat-005",
            "title": {
                "en": "National Means Cum-Merit Scholarship Scheme (NMMSS)",
                "hi": "राष्ट्रीय मींस कम-मेरिट छात्रवृत्ति योजना (NMMSS)"
            },
            "domicile": "All India",
            "type": "Scholarship",
            "official_link": "https://education.gov.in/"
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

    # Universal matching logic: returns matching state policies plus all national schemes
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
