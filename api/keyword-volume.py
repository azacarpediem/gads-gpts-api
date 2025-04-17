from google_ads_client import get_keyword_ideas

def handler(request):
    try:
        req_json = request.get_json()
        keyword = req_json.get("keyword")
        result = get_keyword_ideas(keyword)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": result
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }
