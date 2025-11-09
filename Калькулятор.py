def simple_calculator():
    print("🎯 Простой калькулятор")
    print("Доступные операции: +, -, *, /, **, %")
    print("Для выхода введите 'exit'")
    
    while True:
        try:
            # Ввод данных
            expression = input("\nВведите выражение: ").strip()
            
            if expression.lower() == 'exit':
                print("Выход из калькулятора")
                break
            
            # Проверка на безопасность (ограничиваем eval)
            allowed_chars = set('0123456789+-*/.%() ')
            if not all(c in allowed_chars for c in expression):
                print("Ошибка: Недопустимые символы в выражении")
                continue
            
            # Вычисление
            result = eval(expression)
            print(f"Результат: {result}")
            
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
        except SyntaxError:
            print("Ошибка: Неправильный синтаксис выражения")
        except Exception as e:
            print(f"Ошибка: {e}")

# Запуск калькулятора
if __name__ == "__main__":
    simple_calculator()