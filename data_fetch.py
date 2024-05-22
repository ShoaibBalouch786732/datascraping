import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []
for i in range(1, 30):
    url = f"https://islamqa.info/en/answers/{i}/interruption-of-wudu"
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Data fetched successfully for question {i}')
        htmlcontent = response.content
        soup = BeautifulSoup(htmlcontent, "html.parser")
        question = "No question found"
        answer = "No answer found"
        summary = "No summary found"
        questionNo = i  
        source = "No source found"
        questionanswer = soup.find_all(attrs={'class': 'content'})
        if len(questionanswer) > 0:
            question = questionanswer[0].text.replace('\n', " ")
        if len(questionanswer) > 1:
            answer = questionanswer[1].text.replace('\n', " ")
        summary_tag = soup.find(attrs={'class': "title is-4 is-size-5-touch"})
        if summary_tag:
            summary = summary_tag.text.replace("\n", " ")
        questionNo_tag = soup.find(attrs={'class': "subtitle has-text-weight-bold has-title-case cursor-pointer tooltip"})
        if questionNo_tag:
            questionNo = int(questionNo_tag.text.replace("\n", " "))
        source_tag = soup.find(attrs={'class': "subtitle is-6 has-text-weight-bold is-capitalized"})
        if source_tag:
            source = source_tag.text.replace("\n", " ").replace('source:', " ")
        data.append({
            'url': url,
            'question #': questionNo,
            'summary': summary,
            'question': question,
            'answer': answer,
            'source': source
        })
    else:
        print(f'Not found for question {i}')
df = pd.DataFrame(data, columns=['url', 'question #', 'summary', 'question', 'answer', 'source'])
df.to_csv('pagedata.csv', index=False)
print("Data saved to pagedata.csv")

                           