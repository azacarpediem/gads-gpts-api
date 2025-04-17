from flask import Flask, request, jsonify
from google_ads_client import get_keyword_ideas

app = Flask(__name__)

@app.route("/api/keyword-volume", methods=["POST"])
def keyword_volume():
    try:
        body = request.get_json()
        keyword = body.get("keyword")

        if not keyword:
            return jsonify({"error": "Missing 'keyword' in request body"}), 400

        result = get_keyword_ideas(keyword)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
