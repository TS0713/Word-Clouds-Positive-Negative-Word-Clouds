# Extracting the Data from E-Commerce Website (product reviews)
import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 

import nltk
# Importing stop words
from nltk.corpus import stopwords

# For visualzing the plots
import matplotlib.pyplot as plt

# Package to needed to create word cloud visualizations
from wordcloud import WordCloud

# creating empty reviews list 
iphone_reviews=[]

for i in range(1,10):
  ip=[]  
  url="https://www.amazon.in/Apple-MacBook-Air-13-3-inch-Integrated/product-reviews/B073Q5R6VR/ref=cm_cr_arp_d_paging_btm_2?showViewpoints=1&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  iphone_reviews=iphone_reviews+ip  # adding the reviews of one page to empty list which in future contains all the reviews


# writng reviews in a text file 
with open("iphone.txt","w",encoding='utf8') as output:
    output.write(str(iphone_reviews))
    
    
    
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(iphone_reviews)

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)



# words that contained in iphone 7 reviews
ip_reviews_words = ip_rev_string.split(" ")

stop_words = stopwords.words('english')

# Loading few more stop words which were needed to remove 
# stop words which we miss in our previous step
with open("E:\\Bokey\\Text Mining\\sw.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")



ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# WordCloud can be performed on the string inputs. That is the reason we have combined 
# entire reviews into single paragraph

# Simple word cloud
wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)


# loading positive words for generating positive word cloud
with open("E:\\Bokey\\Bharani_Assignment\\Twitter\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]


# loading Negative words for generating positive word cloud
with open("E:\\Bokey\\Bharani_Assignment\\Twitter\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

