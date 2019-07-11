from FileOperator import FileOperator
from ParserHtml import ParserHtml


def main():
    fo = FileOperator()
    files: list = fo.show_target_file()
    work_pattern = int(input("headタグ内に別タグを挿入する(未実装): 1 挿入されたタグを確認する: 2 "))
    ph = ParserHtml(files)
    if work_pattern == 1:
        pass
    else:
        results: dict = ph.insert_tag_check()
        fo.out_put_csv(results)


if __name__ == '__main__':
    main()
