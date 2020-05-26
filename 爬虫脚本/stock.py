#coding:utf-8
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
    browser.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")
    for i in range(199):
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
            temp["序号"] = re[0]
            temp["代码"] =re[1]
            temp["名称"] =re[2]
            temp["最新价"] =re[4]
            temp["涨跌幅"] =re[5]
            temp["涨跌额"] =re[6]
            temp["成交量"] =re[7]
            temp["成交额"] =re[8]
            temp["振幅"] =re[9]
            temp["最高"] =re[10]
            temp["最低"] =re[11]
            temp["今开"] =re[12]
            temp["昨收"] =re[13]
            temp["量比"] =re[14]
            temp["换手率"] =re[15]
            temp["市盈率"] =re[16]
            temp["市净率"] =re[17]
            result.append(temp)
        print("page "+str(i+1)+" successful!")
        button.click()
    with open("20200522.json","w") as file:
        file.write(json.dumps(result,indent=2,ensure_ascii=False))
except TimeoutException:
    print("error")
finally:
    browser.close()
