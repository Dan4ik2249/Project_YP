import csv

path = input("Введи полный путь до файла, либо, закинь в папку проекта и тогда только имя файла: ")


def searcher(reader, quest):
    i = 0
    with open ("info.csv", mode="w") as w_file:
        writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        for row in reader:
            if i == 0:
                heading = row
                print(str(*heading).split(';'))
                writer.writerow(str(*heading).split(';'))
            i += 1
            if quest in row[0]:
                # тут использую split() для того, чтобы порубить строки по разделителю (";")
                print(row[0].split(";"))
                writer.writerow(row[0].split(";"))
            else:
                pass
        
        


def main():
    quest = input("Введи что нужно найти в файле? ")
    with open(f'{path}.csv') as f:
        reader = csv.reader(f)
        searcher(reader, quest)


if __name__ == "__main__":
    main()