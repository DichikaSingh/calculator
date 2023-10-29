import io

def calculate():
    operator= input("Choose oprator to perform opration(+, -, *, /, **)\n")
    First_num= float(input("First number \n"))
    Second_num= float(input("Second number \n"))
    result= 0
    if operator== "+":
        result = First_num + Second_num
        print(round(result,3))  
    elif operator== "-":
        result= First_num - Second_num
        print(round(result,3)) 
    elif operator== "*":
        result= First_num * Second_num
        print(round(result,3)) 
    elif operator== "/":
        result= First_num / Second_num
        print(round(result,3))
    elif operator== "**":
        result=First_num ** Second_num
        print(round(result))
    else :
        print("Invalid operator, choose again")
