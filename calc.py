def main():
    print("**********CALCULATOR**********")
    a = input("Enter the first Number \n")
    b = input("Enter the second Number \n")
    print("choose the operation operation\n+,-,/,*")
    o = input()
    if o == "+":
       print('The result is:\n',int(a) + int(b))
    
    if o == "-":
       print('The result is:\n',int(a) - int(b))
    
    if o == "*":
       print('The result is:\n',int(a) * int(b))
    
    if o == "/":
       print('The result is:\n',int(a) / int(b))  

while True:
    main()
    if input("Repeat the program? (Y/N)").stdrip().upper() != 'Y':
        break    