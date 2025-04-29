import time
import requests

def ping_url(url):
    try:
        response = requests.get(url)
        print(f"[{time.strftime('%H:%M:%S')}] {url} - {response.status_code}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error: {e}")

if __name__ == "__main__":
    url = "https://verbose-eureka-69wx7xpv6vg5f5pg9.github.dev"  # Ganti dengan URL kamu
    interval = 10  # detik

    while True:
        ping_url(url)
        time.sleep(interval)
