from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# 상위 디렉토리를 sys.path에 추가하여 google_ads_client 모듈을 임포트할 수 있도록 합니다
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from google_ads_client import get_keyword_ideas

# 정적 파일 디렉토리 경로 설정
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, static_folder=static_folder, static_url_path='')
CORS(app)  # CORS 활성화

# 메인 페이지
@app.route('/')
def index():
    return app.send_static_file('index.html')

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

if __name__ == "__main__":
    print("🚀 API 서버 시작 - http://localhost:5000")
    print(f"정적 파일 경로: {static_folder}")
    app.run(debug=True)
