from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# Selenium サーバー (Remote WebDriver) の設定
selenium_url = "http://selenium:4444/wd/hub"
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ブラウザを表示するための設定
chrome_options.add_argument("--start-maximized")  # ブラウザを最大化
chrome_options.add_argument("--disable-infobars")  # 情報バーを無効化
chrome_options.add_argument("--disable-extensions")  # 拡張機能を無効化

driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)
count = 0
# while True:
#     driver.get("https://www.google.com")
#     sleep(1)
#     driver.get("https://tsh.is.oit.ac.jp/?act=home")
#     sleep(1)
#     driver.get("http://abehiroshi.la.coocan.jp")
#     sleep(1)
#     count += 1
#     if count  == 5:
#         break
driver.get("https://tsh.is.oit.ac.jp/?act=home")
try:
    table=driver.find_elements(By.XPATH,'/html/body/table')
    element=table[1].find_elements(By.XPATH,'//tbody/tr/td')
    el=table[1].find_elements(By.XPATH,'//div/table/tbody/tr')
    with open("kenkyuusitu.txt", "w", encoding="utf-8") as f:
        for e in el:
            f.write(e.text + "\n")
except NoSuchElementException:
    print("END")

# driver.save_screenshot("screenshot.png")

print(driver.title)
sleep(2)
driver.quit()
