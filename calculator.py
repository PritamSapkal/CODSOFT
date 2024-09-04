while True:
    a=int(input("\nEnter first number:"))
    b=int(input("enter second number:"))
    c=input("Enter operation which you want to perform (+,-,*,/) :")
    if c=='+':
      print("Addition is :",a+b)
    elif c=='-':
      print("Substraction is :",a-b)
    elif c=='*':
      print("Multiplication is :",a*b)
    elif c=='/':
      print("Division is :",a/b)
    else :
      print("Wrong Choice ! \n Please enter (+,-,*,/) this operation.")                
