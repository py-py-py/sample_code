from qiita import Crawler
from OutPutCsv import OutPutCsv

def main():

    crawler = Crawler()
    results = crawler.get_trend_data()
    output = OutPutCsv(results)
    output.output_csv()

if __name__ == "__main__":
    main()
