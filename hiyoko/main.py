from FileOperator import FileOperator
from ParserHtml import ParserHtml


def main():
    fo = FileOperator()
    files: list = fo.show_target_file()
    work_pattern = int(input("headタグ内に別タグを挿入する(未実装): 1 挿入されたタグを確認する: 2 "))
    ph = ParserHtml(files)
    if work_pattern == 1:
        pass
    elif work_pattern == 2:
        results: dict = ph.insert_tag_check()
        fo.out_put_csv(results)
    else:
        return "1 または 2以外の数字が押されました。どちらかを選んでください。"


if __name__ == '__main__':
    main()
