def check_brackets(expression):
    stack = []
    bracket_map = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in bracket_map:  # Якщо символ є відкритою дужкою
            stack.append(char)
        elif char in bracket_map.values():  # Якщо символ є закритою дужкою
            if not stack or bracket_map[stack.pop()] != char:
                return f"{expression}: Несиметрично"

    if stack:
        return f"{expression}: Несиметрично"
    else:
        return f"{expression}: Симетрично"

# Приклади для тестування
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for exp in expressions:
    print(check_brackets(exp))
