import csv

def main():
    src_filename = input("Введите имя исходного csv-файла (например, contacts.csv): ")
    src_encoding = input("Введите текущую кодировку исходного файла (например, utf-8-sig или cp1251): ")
    src_delimiter = input("Введите текущий разделитель исходного файла (например, ;): ")
    
    new_encoding = input("Введите новую кодировку (например, utf-8 или cp1251): ")
    new_delimiter = input("Введите новый разделитель (например, , или \\t): ")
    new_filename = input("Введите имя нового файла (например, result.csv): ")

    if new_delimiter == "\\t":
        new_delimiter = "\t"

    try:
        with open(src_filename, mode="r", encoding=src_encoding, newline="") as infile:
            reader = csv.reader(infile, delimiter=src_delimiter)
            data = list(reader)

        with open(new_filename, mode="w", encoding=new_encoding, newline="") as outfile:
            writer = csv.writer(outfile, delimiter=new_delimiter)
            writer.writerows(data)

        print(f"\nФайл успешно конвертирован и сохранён как '{new_filename}'.")

    except FileNotFoundError:
        print(f"Ошибка: файл '{src_filename}' не найден.")
    except LookupError:
        print("Ошибка: указана несуществующая кодировка.")
    except UnicodeDecodeError:
        print("Ошибка декодирования: неверно указана исходная кодировка файла.")

if __name__ == "__main__":
    main()
