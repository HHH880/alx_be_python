def perform_operation(num1, num2, operation):
    if operation == 'add':
         return num1 + num2
    elif operation == 'substract':
         return num2-num1
    elif operation == 'multiply':
         return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
             return "DIVISION_NOT_ZERO"
         return num2 / num1
        
