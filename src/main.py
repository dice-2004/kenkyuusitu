from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

I__dict = {
    "データサイエンス学科": "【ID】",
    "実世界情報学科": "【IR】",
    "情報知能学科": "【IC】",
    "情報システム学科": "【IS】",
    "ネットワークデザイン学科": "【IN】",
    "情報メディア学科": "【IM】",
    "共通教育": "【NONE】",
}

selenium_url = "http://selenium:4444/wd/hub"
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
driver.get("https://tsh.is.oit.ac.jp/?act=home")


try:
    table = driver.find_elements(By.XPATH, "/html/body/table")
    element = table[1].find_elements(By.XPATH, "//tbody/tr/td")
    el = table[1].find_elements(By.XPATH, "//div/table/tbody/tr")
    content = el[1].text
    content_list = []
    content = content.split("\n")
    for S in content:
        content_list.append(S.split(" "))
    flag = 0
    with open("kenkyuusitu.txt", "w", encoding="utf-8") as f:
        for S in content_list:
            if S[0] == "ズオン":
                S[0] = "ズオン・クワン・タン"
                S.remove(S[1])
                S.remove(S[1])
            flag=1

            if S[0] in I__dict:
                S[0] = I__dict[S[0]]
                data=S[0]

            elif "\u3000" in S[0] or flag == 1:
                flag = 0
                S[0] = S[0].replace("\u3000", " ")  # 全角スペースを半角スペースに変換
                # data= f"{S[0]:<20} {S[2]:<3} {S[3]:<20} "
                data=str(S)

            else:
                data = str(S)
                pass
            f.write(data + "\n")


except NoSuchElementException:
    print("END")

# driver.save_screenshot("screenshot.png")

print(driver.title)
sleep(2)
driver.quit()
