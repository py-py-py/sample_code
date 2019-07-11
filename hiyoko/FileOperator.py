import os
import csv
from typing import List


class FileOperator(object):

    def show_target_file(self) -> list:
        currentdir: str = os.getcwd()
        file_contents: List[str] = os.listdir(currentdir)
        target_files = [
            file_content for file_content in file_contents if (".php" in file_content) or (".html" in file_content)]
        return target_files

    def out_put_csv(self, result_dict):
        csv_header = [
            "ファイル名", "headタグ内", "結果"
        ]
        csv_data = [csv_header]
        with open("result.csv", "w", encoding="utf-8_sig") as f:
            writer = csv.writer(f, lineterminator="\n")
            for key in result_dict.keys():
                tmp_data: list = [
                    result_dict[key]["file_name"],
                    result_dict[key]["head_tag_content"],
                    result_dict[key]["check"],
                ]
                csv_data.append(tmp_data)
            writer.writerows(csv_data)


def main():
    """
    it's for test code
    :return:
    """
    fo = FileOperator()
    files = fo.show_target_file()
    for file in files:
        print(file)


if __name__ == '__main__':
    main()
