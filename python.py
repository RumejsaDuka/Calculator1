def calculator():
    
    num1 = float(input("Shkruaj numrin e parë: "))
    oper = input("Shkruaj operatorin (+, -, *, /): ")
    num2 = float(input("Shkruaj numrin e dytë: "))
    
    if oper == "+":
        result = num1 + num2
    elif oper == "-":
        result = num1 - num2
    elif oper == "*":
        result = num1 * num2
    elif oper == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Gabim: /0"
    else:
        result = "Operator i gabuar!"
    
    print( result)

# Thirr funksionin
calculator()
