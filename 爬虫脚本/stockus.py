#coding:gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
#proxy = "127.0.0.1:8080"
browser = webdriver.Chrome()# initialization
wait = WebDriverWait(browser,10)
result = []
try:
    browser.get("http://quote.eastmoney.com/center/gridlist.html#us_wellknown")
    for i in range(19):
        time.sleep(1)
        stocks = wait.until(EC.presence_of_element_located((By.ID,"table_wrapper-table"))) 
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.next")))
        html = browser.page_source
        soup = BeautifulSoup(html,"html.parser")
        table = soup.select("#table_wrapper-table")
        tbody = table[0].find("tbody")
        trs = tbody.find_all("tr")
        for tr in trs:
            temp={}
            re = []
            for td in tr:
                re.append(td.text)
            temp["���"] = re[0]
            temp["����"] =re[1]
            temp["���¼�(��Ԫ)"] =re[2]
            temp["�ǵ���"] =re[3]
            temp["�ǵ���"] =re[4]
            temp["���̼�"] =re[5]
            temp["���"] =re[6]
            temp["���"] =re[7]
            temp["����"] =re[8]
            temp["����ֵ(��Ԫ)"] =re[9]
            temp["��ӯ��"] =re[10]
            result.append(temp)
        print("page "+str(i+1)+" successful!")
        button.click()
    with open("us.json","w") as file:
        file.write(json.dumps(result,indent=2,ensure_ascii=False))
except TimeoutException:
    print("error")
finally:
    browser.close()

