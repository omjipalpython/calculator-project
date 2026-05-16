n = float(input("Enter a first number : "))
v = float(input("Enter a Second  number : "))
x = str(input("Choose the operator:\n+ :→ Addition\n- :→ Subtraction\n* :→ Multiplication \n/ :→ Division\n% :→ Remainder\n==  : " ))
if x == "+" :
    print("Answer : ",v+n)
elif x == "-" :
    print("Answer : ",v-n)
elif x == "*" :
    print("Answer : ",v*n)
elif x == "/" :
    print("Answer : ",v/n)
elif x == "%" :
    print("Answer : ",v%n)
else :
    print("SOMETHING ERROR")