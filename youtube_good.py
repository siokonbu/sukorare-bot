from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests, bs4
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from user_info import mail_address, password

# mail_address = '**************'
# password = '***************'
url = 'https://www.youtube.com/user/eguri89/videos'
comment = '瀬戸弘司さん最高'

# ブラウザを開く
driver = webdriver.Chrome(executable_path='./chromedriver')

# youtubeログインページを開く
driver.get('https://accounts.google.com/signin/v2/identifier?passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dja%26next%3D%252F%253Fhl%253Dja%2526gl%253DJP&uilel=3&hl=ja&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

# windowサイズ最大化
driver.maximize_window()

for i in range(10):
    try:
        # メールアドレスを入力
        driver.find_elements_by_css_selector('#identifierId')[0].send_keys(mail_address)
        # 「次へ」をクリックする
        driver.find_elements_by_css_selector('#identifierId')[0].send_keys(Keys.ENTER)
        break

    except (IndexError, ElementNotInteractableException, WebDriverException):
        sleep(1)



for i in range(10):
    try:
        # passwordを入力
        driver.find_elements_by_css_selector('#password input')[0].send_keys(password)
        # 「次へ」をクリックする
        driver.find_elements_by_css_selector('#password input')[0].send_keys(Keys.ENTER)
        break

    except (IndexError, ElementNotInteractableException, WebDriverException):
        sleep(1)

sleep(5)

# 気に入られたいユーザのページへ
driver.get(url)

for i in range(10):
    try:
        # 最新の動画をクリック
        driver.find_elements_by_css_selector('#items #img')[0].click()
        break

    except (IndexError, ElementNotInteractableException, WebDriverException):
        sleep(1)

# 最新の動画ページ
for i in range(10):
    try:
        # goodボタンが押されているか確認
        is_pressed = driver.find_elements_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a > #button')[0].get_attribute('aria-pressed')
        if is_pressed == 'false':
            # goodボタンをクリックする
            driver.find_elements_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a')[0].click()
            print('goodボタンクリック')

            # 動画再生を止める
            driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)

            # スクロール
            for i in range(10):
                try:
                    driver.execute_script("window.scrollBy(0,100)")
                    element = driver.find_elements_by_css_selector('#placeholder-area')[0]
                    actions = ActionChains(driver)
                    actions.move_to_element(element)
                    actions.perform()
                    break

                except (IndexError, ElementNotInteractableException, WebDriverException):
                    sleep(1)

            # コメント送信
            for i in range(10):
                try:
                    # comment欄クリック
                    driver.find_elements_by_css_selector('#simplebox-placeholder')[0].click()
                    for i in range(10):
                        try:
                            # スクロールしながら
                            driver.execute_script("window.scrollBy(0,20)")
                            # comment入力
                            driver.execute_script('document.querySelector("#contenteditable-textarea").innerHTML = "'+str(comment)+'";')
                            # コメントボタン有効化
                            driver.execute_script('document.querySelector("#submit-button").removeAttribute("disabled");')
                            # コメントボタンクリック
                            driver.find_elements_by_css_selector('#submit-button > a')[0].click()
                            print('コメント送信')
                            sleep(10)
                            break

                        except (IndexError, ElementNotInteractableException, WebDriverException):
                            sleep(1)

                    break

                except (IndexError, ElementNotInteractableException, WebDriverException):
                    sleep(1)

        break

    except (IndexError, ElementNotInteractableException, WebDriverException):
        sleep(1)

#ブラウザを閉じる
driver.close()
