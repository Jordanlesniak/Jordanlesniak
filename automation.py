from selenium import webdriver
import time
import random

import os
import urllib

# recaptcha libraries
import pydub
import speech_recognition as sr
# selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# custom patch libraries
import patch



web = webdriver.Chrome()

def delay(waiting_time=5):
    web.implicitly_wait(waiting_time)

web.get('https://www.cityofeastlansing.com/FormCenter/ELPD-15/Overnight-Parking-Requests-77')

time.sleep(2)

firstname = 'Jordan'
first = web.find_element_by_xpath('//*[@id="e_1"]')
first.send_keys(firstname)

delay()

lastname = 'lesniak'
last = web.find_element_by_xpath('//*[@id="e_2"]')
last.send_keys(lastname)

delay()

phonenum = '810-627-1083'
phone = web.find_element_by_xpath('//*[@id="e_3"]')
phone.send_keys(phonenum)

delay()

my_email = 'jordanlesniak99@gmail.com'
email = web.find_element_by_xpath('//*[@id="e_4"]')
email.send_keys(my_email)

delay()

address_list = [539, 540, 545, 546, 556, 557, 569]
rand_num = random.randint(0,6)
address_num = address_list[rand_num]
my_address = ' spartan ave'
add = web.find_element_by_xpath('//*[@id="e_5"]')
add.send_keys(address_num)
add.send_keys(my_address)

delay()

street_name = 'Spartan'
street = web.find_element_by_xpath('//*[@id="e_9"]')
street.send_keys(street_name)

delay()

plate_num = 'CHV7151'
plate = web.find_element_by_xpath('//*[@id="e_11"]')
plate.send_keys(plate_num)

delay()

my_state = 'Michigan'
state = web.find_element_by_xpath('//*[@id="e_12"]')
state.send_keys(my_state)

delay()

make  = 'Ford'
brand = web.find_element_by_xpath('//*[@id="e_13"]')
brand.send_keys(make)

delay()

model = 'F-150'
style = web.find_element_by_xpath('//*[@id="e_14"]')
style.send_keys(model)

delay()

my_color = 'black'
color = web.find_element_by_xpath('//*[@id="e_15"]')
color.send_keys(my_color)

delay()

receipt_email = my_email
receipt = web.find_element_by_xpath('//*[@id="wantCopyAddress"]')
receipt.send_keys(receipt_email)

delay()

submit_button = web.find_element_by_xpath('//*[@id="btnFormSubmit"]/span')
submit_button.click()

'''

if __name__ == "__main__":
    # download latest chromedriver, please ensure that your chrome is up to date
    while True:
        try:
            # create chrome driver
            driver = webdriver.Chrome(os.path.normpath(os.getcwd() + "\\webdriver\\chromedriver.exe"))
            delay()
            # go to website
            driver.get('https://www.cityofeastlansing.com/FormCenter/ELPD-15/Overnight-Parking-Requests-77')
            break
        except Exception:
            # patch chromedriver if not available or outdated
            try:
                driver
            except NameError:
                is_patched = patch.download_latest_chromedriver()
            else:
                is_patched = patch.download_latest_chromedriver(driver.capabilities['version'])
            if not is_patched:
                print("[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:"
                      "https://chromedriver.chromium.org/downloads")
                break

    # main program
    # switch to recaptcha frame
    frames = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    delay()

    # click on checkbox to activate recaptcha
    driver.find_element_by_class_name("recaptcha-checkbox-border").click()

    # switch to recaptcha audio control frame
    driver.switch_to.default_content()
    #frames = driver.find_element_by_xpath('//*[@id="recaptcha-audio-button"]').find_elements_by_tag_name("iframe")
    frames = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button').find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    delay()

    # click on audio challenge
    driver.find_element_by_id("recaptcha-audio-button").click()

    # switch to recaptcha audio challenge frame
    driver.switch_to.default_content()
    frames = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[-1])
    delay()

    # get the mp3 audio file
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s" % src)

    # download the mp3 audio file from the source
    urllib.request.urlretrieve(src, os.path.normpath(os.getcwd() + "\\sample.mp3"))
    delay()

    # load downloaded mp3 audio file as .wav
    try:
        sound = pydub.AudioSegment.from_mp3(os.path.normpath(os.getcwd() + "\\sample.mp3"))
        sound.export(os.path.normpath(os.getcwd() + "\\sample.wav"), format="wav")
        sample_audio = sr.AudioFile(os.path.normpath(os.getcwd() + "\\sample.wav"))
    except Exception:
        print("[-] Please run program as administrator or download ffmpeg manually, "
              "http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/")

    # translate audio to text with google voice recognition
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print("[INFO] Recaptcha Passcode: %s" % key)

    # key in results and submit
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    delay()
    driver.find_element_by_id("recaptcha-demo-submit").click()
    delay()
'''
