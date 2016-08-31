import feedparser
url = "http://www.reddit.com/r/python/.rss"
d = feedparser.parse(url)
for post in d.entries:
  print post.title
