from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    urls = [
        "https://chouseisan.com/s?h=5e04f4fe5a8644b193fa06dc00116256",  # 9月の調整さん
        "https://chouseisan.com/s?h=94277113268548c693a06e6318a2986c",  # 10月
    ]
    data = {}
    for url in urls:
        driver.get(url)
        table = driver.find_element(By.ID, 'nittei')
        trs = table.find_elements(By.TAG_NAME,'tr')

        member = []
        for td in trs[0].find_elements(By.TAG_NAME, "td")[4:]:
            member.append(td.text)


        for tr in trs[1:-1]:
            tds = tr.find_elements(By.TAG_NAME, "td")
            date = tds[0].text.split('(')[0]
            ok = int(tds[1].text[0])
            mention = []
            for i, td in enumerate(tds[4:]):
                if td.find_element(By.TAG_NAME, "img").get_attribute("src")[-5] != "x":
                    mention.append(member[i])
            data[date] = { "ok": ok, "mention": mention }

    driver.quit()
    return data