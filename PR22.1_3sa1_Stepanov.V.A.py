import csv

def main():
    try:
        n = int(input("Введите количество контактов: "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        return

    filename = "contacts.csv"
    
    with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        
        writer.writerow(["name", "contact"])
        
        for i in range(1, n + 1):
            print(f"\nКонтакт №{i}:")
            name = input("Введите название контакта: ")
            contact = input("Введите сам контакт (телефон, email и т.д.): ")
            writer.writerow([name, contact])

    print(f"\nДанные успешно сохранены в файл {filename}")

if __name__ == "__main__":
    main()
