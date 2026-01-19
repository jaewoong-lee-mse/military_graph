from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_page_warp():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # 1. 초기 접속
        driver.get("https://www.mma.go.kr/board/boardList.do?gesipan_id=2")
        time.sleep(2)
        
        # 1페이지 첫 번째 글 제목 확인
        first_page_title = driver.find_element(By.CLASS_NAME, "subject").text
        print(f"[1페이지 첫 글]: {first_page_title}")

        # 2. JS 함수로 2페이지 이동 실행
        print("\n>>> 2페이지로 JS 워프 실행!")
        driver.execute_script("fn_PageList(2)") 
        time.sleep(3) # 페이지가 로딩될 때까지 충분히 대기

        # 3. 2페이지 첫 번째 글 제목 확인
        second_page_title = driver.find_element(By.CLASS_NAME, "subject").text
        print(f"[2페이지 첫 글]: {second_page_title}")

        # 4. 검증
        if first_page_title != second_page_title:
            print("\n✅ 성공: 페이지가 정상적으로 이동되었습니다!")
        else:
            print("\n❌ 실패: 제목이 같습니다. 페이지가 이동되지 않았습니다.")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_page_warp()