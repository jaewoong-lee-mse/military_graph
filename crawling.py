
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. 크롬 드라이버 자동 설치 및 서비스 설정
try:
    print("크롬 드라이버를 준비 중입니다...")
    service = Service(ChromeDriverManager().install())
    
    # 2. 브라우저 실행
    driver = webdriver.Chrome(service=service)
    
    print("성공! 병무청 사이트로 이동합니다.")
    # 3. 테스트 사이트(병무청) 접속
    driver.get("https://www.mma.go.kr")
    
    # 4. 5초간 대기 (브라우저가 떴는지 확인하는 시간)
    time.sleep(5)
    print("테스트 완료. 브라우저를 종료합니다.")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")

finally:
    # 5. 브라우저 종료
    if 'driver' in locals():
        driver.quit()