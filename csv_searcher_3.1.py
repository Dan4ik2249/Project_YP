import csv
from encodings import utf_8

path = input("Введи полный путь до файла или имя файла, если он находится в папке программы: ")

def searcher(reader, quest, param, quest_1=0, param_1=0, quest_2=0, param_2=0):
    i = 0
    with open ("info.csv", mode="w", encoding='utf_8') as w_file:
        
        for row in reader:
            if i == 0:
                heading = row
                writer = csv.DictWriter(w_file, delimiter=";", extrasaction='ignore', fieldnames = list(heading.keys()))
                writer.writeheader()
                i += 1
            
            if param_1==0 and param_2==0 and quest_1==0 and quest_2==0:   
                if row[f'{quest}'] == param:
                    writer.writerow(row)
                else:
                    pass
            
            elif param_2==0 and quest_2==0:
                if row[f'{quest}'] == param and row[f'{quest_1}'] == param_1:
                    writer.writerow(row)
                else:
                    pass
                
            else:
                if row[f'{quest}'] == param and row[f'{quest_1}'] == param_1 and row[f'{quest_2}'] == param_2:
                    writer.writerow(row)
                else:
                    pass
        
def myprint():
    print("1. Посмотреть доступные критерии поиска.")
    print("2. Запуск поиска.")
    print("0. Закрыть программу")

def main():
    myprint()
    print()
    menu = int(input())
    while menu<0 or menu>2:
        print("Ошибка: выбранный пункт отсутствует.")
        menu = input("Попробуйте еще раз")
    
    while menu != 0:
        match menu:
            case 1:
                print("Доступны следующие параметры поиска")
                print("ИМЯ | ФАМИЛИЯ | ПОЛ(М/Ж) | ЛЕТ | СТРАНА | ГОРОД | ОТКРЫТЫ СООБЩЕНИЯ(да/нет) | ОТКРЫТЫЙ ПРОФИЛЬ(да/нет) | ПРЕМИУМ(да/нет) | ПРИВАТ(да/нет) | VIP(да/нет)")
                myprint()
                menu = int(input())
            
            case 2:
                choise = int(input("Введите количество критериев поиска(от 1 до 3х): "))
                while choise<0 or choise>3:
                    print("Ошибка: введенное число не принадлежит диапазону от 1 до 3х")
                    choise = input("Введите количество критериев поиска(от 1 до 3х): ")
    
                with open(f'{path}.csv', encoding='utf_8') as f:
                    reader = csv.DictReader(f, delimiter= ';')
                    while choise != 0:
                        match choise:
                            case 1:
                                quest = input("Введите параметр поиска(заглавными буквами): ")
                                param = input("Введи что нужно найти в файле? ")
                                searcher(reader, quest, param)
                                break
                
                            case 2:
                                quest = input("Введите параметр поиска(заглавными буквами): ")
                                param = input("Введи что нужно найти в файле? ")
                                quest_1 = input("Введите параметр поиска(заглавными буквами): ")
                                param_1 = input("Введи что нужно найти в файле? ")
                                searcher(reader, quest, param, quest_1, param_1)
                                break
                
                            case 3:
                                quest = input("Введите параметр поиска(заглавными буквами): ")
                                param = input("Введи что нужно найти в файле? ")
                                quest_1 = input("Введите параметр поиска(заглавными буквами): ")
                                param_1 = input("Введи что нужно найти в файле? ")
                                quest_2 = input("Введите параметр поиска(заглавными буквами): ")
                                param_2 = input("Введи что нужно найти в файле? ")
                                searcher(reader, quest, param, quest_1, param_1, quest_2, param_2)
                                break
                print("Поиск завершён. Обратитесь к файлу info.csv")
                break
            
if __name__ == "__main__":
    main()