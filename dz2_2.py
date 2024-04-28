from collections import deque

def is_palindrome(s):
    # Видалення пробілів і переведення рядка до нижнього регістру
    s = ''.join(s.split()).lower()
    
    # Створення двосторонньої черги з символів рядка
    d = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Тестування функції
test_strings = ["A man a plan a canal Panama", "Racecar", "No lemon, no melon", "Hello"]
for string in test_strings:
    print(f"'{string}' -> {is_palindrome(string)}")
