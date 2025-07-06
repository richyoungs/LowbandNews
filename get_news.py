import feedparser
from datetime import datetime

feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
lines = []

lines.append("== LOWBAND.NEW HEADLINES ==")
lines.append(" ")
for entry in feed.entries[:5]:
    title = entry.title.strip()

    while len(title) > 40:
        lines.append(title[:40])
        title = title[40:]
    lines.append(title)
    lines.append(" ")

lines.append("Updated: " + datetime.now().strftime("%I:%M %P"))
lines.append("=" * 40)

with open("news.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
