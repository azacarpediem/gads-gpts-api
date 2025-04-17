"""
API 요청 테스트 스크립트
"""
import requests
import json

def test_keyword_volume_api(keyword):
    """키워드 분석 API 테스트"""
    url = "http://localhost:5000/api/keyword-volume"
    headers = {"Content-Type": "application/json"}
    data = {"keyword": keyword}
    
    print(f"🔍 '{keyword}' 키워드에 대한 분석 요청 중...")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # HTTP 오류 체크
        
        result = response.json()
        print(f"✅ 응답 성공!")
        print(f"📊 {len(result)}개의 키워드 아이디어를 찾았습니다.")
        
        # 상위 10개 키워드만 출력
        print("\n상위 10개 키워드:")
        for i, item in enumerate(result[:10], 1):
            print(f"{i}. {item['keyword']} - 월 {item['monthly_searches']}회 검색, 경쟁도: {item['competition']}, CPC: {item['cpc']}원")
        
        return result
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다. API 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        if hasattr(e, 'response'):
            print(f"서버 응답: {e.response.text}")

if __name__ == "__main__":
    keyword = "노트북"  # 여기에 분석하고 싶은 키워드를 입력하세요
    test_keyword_volume_api(keyword) 