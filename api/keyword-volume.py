import json
from google_ads_client import get_keyword_ideas

def handler(request):
    try:
        body = json.loads(request.body.decode("utf-8"))
        keyword = body.get("keyword")
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
