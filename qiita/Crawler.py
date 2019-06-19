from selenium import webdriver


class Crawler(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.url = "https://qiita.com/"
        self.result = []

    def get_trend_data(self):
        self.driver.get(self.url)
        trends = self.driver.find_elements_by_class_name("tr-Item_body")
        for trend in trends:
            data: list = []
            items = trend.find_elements_by_tag_name("a")
            href = items[0].get_attribute("href")
            title = items[0].text
            author = items[1].text
            data.append(title)
            data.append(href)
            data.append(author)
            self.result.append(data)
            
        return self.result

def main():
    crawler = Crawler()
    results = crawler.get_trend_data()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
