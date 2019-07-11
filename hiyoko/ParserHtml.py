from bs4 import BeautifulSoup
import csv


class ParserHtml(object):

    def __init__(self, files: list):
        self.files = files
        self.out_put = {}

    def insert_tag_check(self):
        html = ""
        with open("result2.csv", "a", encoding="utf-8_sig", newline="") as f:
            csv_header = [
                "ファイル名", "headタグ内", "結果"
            ]
            writer = csv.writer(f)
            writer.writerow(csv_header)
            for file in self.files:
                open_file_for_beautifulsoup = open(file, "r", encoding="utf-8")
                html = open_file_for_beautifulsoup.read()
                open_file_for_beautifulsoup.close()
                html = BeautifulSoup(html, "html.parser")
                heads = html.find_all("head")
                result: dict = {}

                result[file] = {
                    "file_name": file,
                    "head_tag_content": "",
                    "check": ""
                }

                for head in heads:
                    result[file]["head_tag_content"] = head
                    
                    """headタグ内に挿入したタグがあるかを文字列の一致で確認する"""
                    if ("Global site tag (gtag.js)" in str(head)) or ("googletagmanager" in str(head)):
                        result[file]["check"] = "○"
                    else:
                        result[file]["check"] = "×"
                csv_data = [
                    result[file]["file_name"],
                    result[file]["head_tag_content"],
                    result[file]["check"]
                ]
                writer.writerow(csv_data)
