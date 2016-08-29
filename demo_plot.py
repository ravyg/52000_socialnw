import nltk
import urllib
import matplotlib
import re
from urllib import urlopen
from nltk import FreqDist
from bs4 import BeautifulSoup
url = "http://www.youtude.com"
html = urlopen(url).read()
# Using Beautiful soup.
soup = BeautifulSoup(html)
raw = soup.get_text()
# raw = nltk.clean_html(html)
raw = raw.replace("\n","")
raw = raw.replace("\t","")

# Remove unicodes.
raw = re.sub(r'[^\x00-\x7F]+',' ', raw)

# Some more processing 
raw = re.sub(r'(.+)[\!\#\@\?\"\'\&\$\(\)\+\_\-\:\;]+\1', r'\1 ', raw)
raw = re.sub(r'([A-Z])', r' \1', raw)


tokens = nltk.word_tokenize(raw)
fdist = FreqDist(tokens)
fdist.plot(50, cumulative=True)

