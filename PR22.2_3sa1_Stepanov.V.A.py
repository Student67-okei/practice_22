import csv

def main():
    filename = "table.csv"
    
    try:
        with open(filename, mode="r", encoding="utf-8-sig") as file:
            reader = csv.reader(file, delimiter=";")
            
            for row in reader:
                print(" | ".join(f"{item:<15}" for item in row))
                
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Убедитесь, что он находится в папке с программой.")
    except UnicodeDecodeError:
        print("Ошибка кодировки. Попробуйте заменить encoding='utf-8-sig' на encoding='cp1251'.")

if __name__ == "__main__":
    main()
