
import requests
from bs4 import BeautifulSoup
#send http request
st_url = "https://ntvkenya.co.ke/news/"
news_page = requests.get(st_url)
print(news_page.status_code)
# parse html content
soup = BeautifulSoup(news_page.content,"html.parser")
# print(soup.prettify())

# Extract headlines by class
headline = soup.find_all(id="video-card_title no_shadow")
for h2_tags in headline:    
    print(h2_tags.text)

#Extract summaries
summaries = soup.find_all("p")
for sum in summaries:
    print(sum.text)



 

