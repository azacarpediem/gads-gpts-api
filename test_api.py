import requests

def test_keyword_volume():
    url = "https://gads-gpts-4542vf4vb-azavios-projects.vercel.app/api/keyword-volume"
    payload = {"keyword": "미백 크림"}
    headers = {"Content-Type": "application/json"}

    resp = requests.post(url, json=payload, headers=headers)
    print(resp.status_code)
    print(resp.json())

test_keyword_volume()
