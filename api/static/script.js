document.addEventListener('DOMContentLoaded', function() {
    const keywordInput = document.getElementById('keyword');
    const searchBtn = document.getElementById('search-btn');
    const loadingElement = document.getElementById('loading');
    const resultsElement = document.getElementById('results');
    const resultCountElement = document.getElementById('result-count');
    const resultsBodyElement = document.getElementById('results-body');
    const errorMessageElement = document.getElementById('error-message');
    
    // 엔터 키 이벤트 처리
    keywordInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            searchKeyword();
        }
    });
    
    // 검색 버튼 클릭 이벤트
    searchBtn.addEventListener('click', searchKeyword);
    
    function searchKeyword() {
        const keyword = keywordInput.value.trim();
        
        if (!keyword) {
            alert('키워드를 입력해주세요.');
            return;
        }
        
        // UI 상태 업데이트
        loadingElement.classList.remove('hidden');
        resultsElement.classList.add('hidden');
        errorMessageElement.classList.add('hidden');
        
        // API 요청 (상대 경로 사용)
        fetch('/api/keyword-volume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ keyword: keyword })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('API 요청 실패');
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            loadingElement.classList.add('hidden');
            errorMessageElement.classList.remove('hidden');
        });
    }
    
    function displayResults(data) {
        // 로딩 숨기기
        loadingElement.classList.add('hidden');
        
        // 결과 수 표시
        resultCountElement.textContent = `총 ${data.length}개의 키워드 아이디어를 찾았습니다.`;
        
        // 테이블 내용 초기화
        resultsBodyElement.innerHTML = '';
        
        // 상위 50개만 표시 (너무 많으면 브라우저 성능 저하 가능성)
        const displayLimit = Math.min(data.length, 50);
        
        // 결과 표시
        for (let i = 0; i < displayLimit; i++) {
            const item = data[i];
            const row = document.createElement('tr');
            
            row.innerHTML = `
                <td>${i + 1}</td>
                <td>${item.keyword}</td>
                <td>${item.monthly_searches}</td>
                <td>${item.competition}</td>
                <td>${parseFloat(item.cpc).toLocaleString('ko-KR', { maximumFractionDigits: 2 })}</td>
            `;
            
            resultsBodyElement.appendChild(row);
        }
        
        // 결과 영역 표시
        resultsElement.classList.remove('hidden');
    }
}); 