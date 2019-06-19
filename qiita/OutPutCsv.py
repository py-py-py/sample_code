import csv

class OutPutCsv(object):

    def __init__(self, data):
        self.data = data
        self.now = datetime.now()
    
    def output_csv(self):
        csv_header = ["タイトル", "URL", "著者"]
        csv_data = []
        csv_data.append(csv_header)
        with open("result.csv", "w", encoding="utf-8_sig") as f:
            writer = csv.writer(f, lineterminator="\n")
            for data in self.data:
                csv_data.append(data)
            writer.writerows(csv_data)
