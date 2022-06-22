from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from twilio.rest import Client
import os


username="turedi19@itu.edu.tr"
pasword = "14594267Gt"
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME-BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")
driver = webdriver.Chrome(chrome_options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
driver.get("https://kepler-beta.itu.edu.tr/ogrenci/")
driver.find_element(by=By.ID,value="ContentPlaceHolder1_tbUserName").send_keys(username)
driver.find_element(by=By.ID,value="ContentPlaceHolder1_tbPassword").send_keys(pasword)
driver.find_element(by= By.CSS_SELECTOR,value="input[type=\"submit\" i]").click()

sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/ul/li[4]/a').click()
sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[1]/div[2]/div[3]/ul/li/div/ul/li[2]/a').click()
sleep(2)
elem = driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[2]/div/div/div[3]/div/div/div/table/tbody')
trs = elem.find_elements(By.TAG_NAME,"tr")
g = open("demofile3.txt", "r")


if trs.__len__()>int(g.read()):
 account_sid = 'AC9e424acd0a50e312f76459d7e100413b'
 auth_token = '413afe6519d130cf2f33eeb7a1aa280e'
 client = Client(account_sid, auth_token)

 message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=trs[trs.__len__()-1].text,
    to='whatsapp:+905454400978'
 )

 print(message.sid)
f = open("demofile3.txt", "w")
f.write(str(trs.__len__()))
f.close()
print (trs.__len__())
driver.quit()
"""driver = webdriver.Chrome("/Users/guven/Desktop/chromedriver")"""