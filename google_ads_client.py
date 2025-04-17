from google.ads.googleads.client import GoogleAdsClient
import os
from tempfile import NamedTemporaryFile

def get_keyword_ideas(keyword):
    yaml_content = f"""developer_token: '{os.getenv("DEVELOPER_TOKEN")}'
client_id: '{os.getenv("CLIENT_ID")}'
client_secret: '{os.getenv("CLIENT_SECRET")}'
refresh_token: '{os.getenv("REFRESH_TOKEN")}'
login_customer_id: '{os.getenv("LOGIN_CUSTOMER_ID")}'
"""

    with NamedTemporaryFile("w+", delete=False) as temp_yaml:
        temp_yaml.write(yaml_content)
        temp_yaml.flush()

        client = GoogleAdsClient.load_from_storage(temp_yaml.name)
        service = client.get_service("KeywordPlanIdeaService")

        request = {
            "customer_id": os.getenv("CUSTOMER_ID"),
            "language": {"resource_name": "languageConstants/1012"},
            "geo_target_constants": ["geoTargetConstants/2840"],
            "keyword_seed": {"keywords": [keyword]},
        }

        response = service.generate_keyword_ideas(request=request)
        result = []
        for idea in response:
            result.append({
                "keyword": idea.text,
                "monthly_searches": idea.keyword_idea_metrics.avg_monthly_searches,
                "competition": idea.keyword_idea_metrics.competition.name,
                "cpc": idea.keyword_idea_metrics.high_top_of_page_bid_micros / 1_000_000
            })
        return result
