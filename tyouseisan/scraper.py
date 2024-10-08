from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    urls = [
        "https://chouseisan.com/s?h=5e04f4fe5a8644b193fa06dc00116256",  # 9月の調整さん
        "https://chouseisan.com/s?h=94277113268548c693a06e6318a2986c",  # 10月
    ]
    data = {}
    for url in urls:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "lxml")
        table = soup.find(id="nittei")
        trs = table.find_all("tr")

        member = []
        for td in trs[0].find_all("td")[4:]:
            member.append(td.text)


        for tr in trs[1:-1]:
            tds = tr.find_all("td")
            date = tds[0].text.split('(')[0]
            ok = int(tds[1].text[0])
            mention = []
            for i, td in enumerate(tds[4:]):
                if td.find("img").attrs["src"][-5] != "x":
                    mention.append(member[i])
            data[date] = { "ok": ok, "mention": mention }

    driver.quit()
    return data