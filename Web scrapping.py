import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://islamqa.info/en/answers/109188/ruling-on-renting-a-trade-licence'


page=requests.get(url)
#  print(page)

soup=BeautifulSoup(page.content,'html.parser')

title=soup.find(class_="title is-4 is-size-5-touch").text.replace("\n","  ")
#print(title)

publishdate=soup.find(class_="subtitle has-text-muted has-title-case").text.replace("\n","  ")
#print(pubdate)

questionnumber=soup.find(class_="subtitle has-text-weight-bold has-title-case cursor-pointer tooltip").text.replace("\n","  ")
#print(questionno)

question=soup.find(class_="single_fatwa__question text-justified").text.replace("\n","  ")
#print(question)


answer=soup.find(class_="single_fatwa__answer").text.replace("\n","  ")
#print(answer)

data=[[url,title,publishdate,questionnumber,question,answer]]
#print(data)

df=pd.DataFrame(data,columns=['URL','Title','PublishDate','QuestionNumber','Question','Answer'])
#print(df)

df.to_csv("final report.csv")
print('ok')