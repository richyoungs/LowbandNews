# Lowband.News

**Lowband.News** is a lightweight, retro-friendly news headline fetcher and server designed to work on modern systems while remaining accessible from vintage computers like the Commodore VIC-20, C64, and C128 using a WiFi modem or terminal software.

This project fetches the latest RSS headlines from a configured news source and serves them as a simple text file over HTTP — ideal for low-bandwidth viewing and BBS-like interfaces.

You can view the software's functionality by using TELNET on the address: 144.48.104.213:2323, which will retrieve the latest headlines that the script has retrieved. 

---

## 🛠 Features

- Fetches headlines from any RSS feed (e.g., NYTimes, BBC, etc.)
- Outputs simple, readable `.txt` files
- Serves headlines locally over HTTP (default port: 8000)
- Compatible with real retro hardware via user port WiFi modem
- Runs on any modern system with Python 3

---

## 📦 Included Files

| File         | Description                                     |
|--------------|-------------------------------------------------|
| `get_news.py`| Fetches headlines and saves to `news.txt`       |
| `server.py`  | Serves the current directory over HTTP          |

---

## 🚀 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/lowbandnews.git
cd lowbandnews
