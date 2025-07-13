import feedparser
from datetime import datetime
from zoneinfo import ZoneInfo
import time

def sanitize_and_pad_line(text):
    text = text.upper()
    text = ''.join(c for c in text if ord(c) < 128)  # remove non-ASCII
    text = text.strip()
    while len(text) < 40:
        text += " "
    return text[:40]

def wrap_headline(title):
    result = []
    title = title.strip().upper()
    while title:
        result.append(sanitize_and_pad_line(title[:40]))
        title = title[40:]
    return result

def generate_news():
    feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    lines = []

    # Header
    lines.append(sanitize_and_pad_line("== LOWBAND.NEWS HEADLINES =="))
    lines.append(sanitize_and_pad_line("----------------------------------------"))

    # Headlines
    for entry in feed.entries[:5]:
        wrapped = wrap_headline(entry.title)
        lines.extend(wrapped)
        lines.append(sanitize_and_pad_line("----------------------------------------"))

    # Footer with local time
    local_time = datetime.now(ZoneInfo("America/New_York"))
    lines.append(sanitize_and_pad_line("UPDATED: " + local_time.strftime("%I:%M %p")))
    lines.append(sanitize_and_pad_line("========================================"))

    # Save to news.txt
    with open("news.txt", "w", newline="\n") as f:
        for line in lines:
            f.write(line + "\n")

def main_loop():
    while True:
        print("Updating headlines...")
        generate_news()
        print("Updated. Waiting 30 minutes...\n")
        time.sleep(1800)  # 30 minutes

main_loop()
