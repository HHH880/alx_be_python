def perform_operation(num1, num2, operation):
    if operation == 'add'.lower():
         return num1 + num2
    if operation == 'substract':
         return num2-num1
    if operation == 'multiply':
         return num1 * num2
    if operation == 'divide'.lower():
        while num1 ==0:
         print("Num1 should not be zero(0)")
         return num2 / num1
        