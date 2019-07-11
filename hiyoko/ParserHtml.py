from bs4 import BeautifulSoup


class ParserHtml(object):

    def __init__(self, files: list):
        self.files = files
        self.out_put = {}

    def insert_tag(self):
        pass

    def insert_tag_check(self) -> dict:
        """
        headタグ内にタグがあるかを確認する
        :return: dict
        """

        html = ""
        for file in self.files:
            with open(file, "r", encoding="utf-8") as f:
                html = f.read()
            html: BeautifulSoup = BeautifulSoup(html, "html.parser")
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
                if "<meta charset" in str(head):
                    result[file]["check"] = "○"
                else:
                    result[file]["check"] = "×"

            self.out_put.update(result)

        return self.out_put
