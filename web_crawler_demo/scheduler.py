import schedule
import time
import subprocess

def run_spider():
    subprocess.run(["scrapy", "crawl", "spider1"], cwd="./web_crawler_demo")

run_spider()
schedule.every(2).minutes.do(run_spider)

while True:
    schedule.run_pending()
    time.sleep(1)
