import json
from google_ads_client import get_keyword_ideas

def handler(request):
    try:
        # 요청 본문을 파싱
        body = json.loads(request.body.decode("utf-8"))
        keyword = body.get("keyword")

        # 키워드가 없으면 에러 반환
        if not keyword:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'keyword' in request body"})
            }

        # 실제 키워드 검색량 조회
        result = get_keyword_ideas(keyword)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
