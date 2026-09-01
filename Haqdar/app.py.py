import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables communication with Member 1's frontend

@app.route("/api/match", methods=['GET'])
def match_opportunities():
    # Capture profile parameters matching Member 1's frontend form
    age = int(request.args.get("age", 0) or 0)
    income = int(request.args.get("income", 9999999) or 9999999)
    category = request.args.get("category", "General")
    state = request.args.get("state", "All India")
    education = request.args.get("education", "")

    eligible_opportunities = []

    try:
        # Professor's robust fallback array structure
        welfare_data = [
            {
                "id": "mah-001",
                "title": {
                    "en": "Post-Matric Scholarship Scheme for SC Students",
                    "hi": "अनुसूचित जाति के छात्रों के लिए पोस्ट-मैट्रिक छात्रवृत्ति योजना"
                },
                "type": "Scholarship",
                "domicile": "Maharashtra",
                "max_income": 250000,
                "target_category": "SC",
                "min_age": 16,
                "max_age": 25,
                "official_link": "https://mahadbtmahait.gov.in/",
                "deadline_days": 45,
            },
            {
                "title": {
                    "en": "Central Sector Scheme of Scholarship for College Students",
                    "hi": "कॉलेज के छात्रों के लिए केंद्रीय क्षेत्र छात्रवृत्ति योजना"
                },
                "type": "Scholarship",
                "domicile": "All India",
                "max_income": 450000,
                "target_category": "General",
                "min_age": 18,
                "max_age": 25,
                "official_link": "https://scholarships.gov.in/",
                "deadline_days": 14,
            }
        ]

        # Process filtering logic safely
        for scheme in welfare_data:
            income_ok = income <= scheme["max_income"]
            category_ok = (scheme["target_category"] == "All") or (scheme["target_category"] == category)
            domicile_ok = (scheme["domicile"] == "All India") or (scheme["domicile"] == state)
            age_ok = (scheme["min_age"] <= age <= scheme["max_age"]) if age > 0 else True

            if income_ok and category_ok and domicile_ok and age_ok:
                eligible_opportunities.append(
                    {
                        "id": scheme.get("id", "sch-00x"),
                        "title": scheme["title"],
                        "type": scheme["type"],
                        "domicile": scheme["domicile"],
                        "official_link": scheme["official_link"]
                    }
                )
    except Exception as e:
        print("Filtering Error:", e)

    return jsonify({"success": True, "count": len(eligible_opportunities), "matches": eligible_opportunities})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)