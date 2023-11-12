import requests
import pandas as pd

from bs4 import BeautifulSoup
data={'Quotes':[] , 'Authors Name':[],'Associated Link':[], 'Associated Tags':[]}
url = 'https://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# quotes
spans=soup.find_all(class_="text")
for quote in soup.find_all(class_="text"):
    print(quote.get_text(strip=True))
    data['Quotes'].append(quote.get_text(strip=True))
    
    
# Author name
Author=soup.find_all('small',class_="author")
for authors in soup.find_all('small',class_="author"):
    print(authors.get_text(strip=True))
    data['Authors Name'].append(authors.get_text(strip=True))


# Authiors Link 
about_links=soup.find_all('a',string="(about)")
for link in about_links:
    href=link.get('href')
    print(href)
    data['Associated Link'].append(href)
    
    
#tags 
keywords_meta = soup.find_all('meta', class_='keywords', itemprop='keywords')
content_values = [tag.get('content') for tag in keywords_meta]
for content_value in content_values:
    print(content_value)
    data['Associated Tags'].append(content_value)
    
# making csv file
df=pd.DataFrame.from_dict(data)
df.to_excel('data.xlsx',index=False)
    
    
    





