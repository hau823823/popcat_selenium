from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import keyboard


options = Options()
options.add_argument("--disable-notifications")
options.add_argument('--disable-gpu') # 禁用gpu加速
options.add_argument('--disable-infobars')  # 禁止策略化
options.add_argument('--no-sandbox')  # 解決DevToolsActivePort文件不存在報錯
options.add_argument('--incognito')  # 無痕模式
options.add_argument('--hide-scrollbars')  # 隱藏滾動條
options.add_argument('--start-maximized') # 視窗最大化
options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 禁用瀏覽器正在被自動化程式控制提示
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')


product_url = 'https://popcat.click/'
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(product_url)

elemClick = driver.find_element_by_xpath("//div[@class='cat-img p']")

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(' '):  # if key ' ' is pressed
            print('Finish')
            break  # finishing the loop
        else:
            elemClick.click()
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break
