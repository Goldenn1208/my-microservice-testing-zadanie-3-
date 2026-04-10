import json

def convert_currency(amount, currency):
    """Логика конвертации для тестов"""
    rates = {"USD": 92.5, "EUR": 100.2}
    if currency not in rates:
        return {"status": "error", "message": "Валюта не поддерживается"}
    if amount < 0:
        return {"status": "error", "message": "Отрицательная сумма"}
    result_rub = round(amount * rates[currency], 2)
    return {
        "status": "success", 
        "data": {"amount": amount, "currency": currency, "result_rub": result_rub}
    }

def main():
    print("--- Микросервис v2.0 ---")
    try:
        curr = input("Валюта (USD/EUR): ").upper()
        amt = float(input(f"Сумма в {curr}: "))
        result = convert_currency(amt, curr)
        print(json.dumps(result, indent=4, ensure_ascii=False))
    except ValueError:
        print(json.dumps({"status": "error", "message": "Не число"}))

if __name__ == "__main__":
    main()