import json
from datetime import datetime

# Функция для записи действий в файл (Issue #5)
def log_event(data):
    with open("log.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {json.dumps(data, ensure_ascii=False)}\n")

def main():
    rates = {"USD": 92.5, "EUR": 100.2}
    print("--- Микросервис Конвертации v1.4 (FINAL) ---")
    
    currency = input("Выберите валюту (USD или EUR): ").upper()
    
    if currency in rates:
        try:
            user_input = input(f"Введите сумму в {currency}: ")
            amount = float(user_input)
            
            # Проверка на отрицательные числа (Issue #4)
            if amount < 0:
                err = {"status": "error", "message": "Отрицательное число"}
                print(json.dumps(err, indent=4, ensure_ascii=False))
                log_event(err)
                return

            result_rub = round(amount * rates[currency], 2)
            
            # Ответ в JSON (Issue #3)
            response = {
                "status": "success",
                "data": {
                    "amount": amount,
                    "currency": currency,
                    "result_rub": result_rub
                }
            }
            print(json.dumps(response, indent=4, ensure_ascii=False))
            log_event(response) # Логируем успех
            
        except ValueError:
            err = {"status": "error", "message": "Введено не число"}
            print(json.dumps(err, indent=4, ensure_ascii=False))
            log_event(err)
    else:
        err = {"status": "error", "message": "Валюта не поддерживается"}
        print(json.dumps(err, indent=4, ensure_ascii=False))
        log_event(err)

if __name__ == "__main__":
    main()