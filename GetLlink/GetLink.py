from time import sleep
from selenium import webdriver


class GetLink(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS()

    def access_site(self):
        self.driver.get(self.url)

    def get_link(self):
        self.access_site()
        result_url = []
        table_count = 1
        len_table = len(self.driver.find_elements_by_class_name("toctree-l1"))
        for _ in range(len_table):
            table_content = self.driver.find_elements_by_xpath(f'//*[@id="the-python-standard-library"]/div/ul/li[{table_count}]/a')
            if len(table_content):
                table_content[0].click()
                result_url.append(self.driver.current_url)
                self.driver.back()
                sleep(1)
            table_count += 1

        return result_url


if __name__ == '__main__':
    url = "https://docs.python.org/ja/3/library/index.html"
    itchan = GetLink(url)
    results = itchan.get_link()
    for result in results:
        print(result)
