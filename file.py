from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from twilio.rest import Client
import os
import boto3
from botocore.exceptions import ClientError
import io





username="turedi19@itu.edu.tr"
pasword = "14594267Gt"
options = Options()
options.headless = True
##options = webdriver.ChromeOptions()
##options.binary_location = os.environ.get("GOOGLE_CHROME-BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")
#driver = webdriver.Chrome(chrome_options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
driver = webdriver.Chrome(options=options, executable_path=r'/Users/guven/Desktop/chromedriver')
driver.get("https://kepler-beta.itu.edu.tr/ogrenci/")
driver.find_element(by=By.ID,value="ContentPlaceHolder1_tbUserName").send_keys(username)
driver.find_element(by=By.ID,value="ContentPlaceHolder1_tbPassword").send_keys(pasword)
driver.find_element(by= By.CSS_SELECTOR,value="input[type=\"submit\" i]").click()

sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/ul/li[4]/a').click()
sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[1]/div[2]/div[3]/ul/li/div/ul/li[2]/a').click()
sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[2]/div/div/div[2]/div/div/div/select/option[2]').click()
sleep(2)
elem = driver.find_element(by=By.XPATH,value='//*[@id="page-wrapper"]/div[2]/div/div/div[3]/div/div/div/table/tbody')
sleep(2)
trs = elem.find_elements(By.TAG_NAME,"tr")
s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id='AKIAWWCP6L7RQMHMHEFJ',
                               aws_secret_access_key='eOygMleKDFGyYwI6CFAIuqJ1vrZA6m8fKIjNJ46h')

S3_BUCKET = 'guvenbucket'
def lambda_handler():
  object_key = "aaa/demofile3.txt"  # replace object key
  file_content = s3_client.get_object(
      Bucket=S3_BUCKET, Key=object_key)["Body"].read()
  return file_content.decode()
w=lambda_handler()
if trs.__len__()>int(w):
 account_sid = 'AC9e424acd0a50e312f76459d7e100413b'
 auth_token = '413afe6519d130cf2f33eeb7a1aa280e'
 client = Client(account_sid, auth_token)

 message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=trs[trs.__len__()-1].text,
    to='whatsapp:+905454400978'
 )

 print(message.sid)
session = boto3.Session(
aws_access_key_id='AKIAWWCP6L7RQMHMHEFJ',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

b =str(trs.__len__())
txt_data = b.encode()

object = s3.Object('guvenbucket', 'aaa/demofile3.txt')

result = object.put(Body=txt_data)
driver.quit()
