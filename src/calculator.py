import io


def calculate():
    while True:
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
        else:
            print("invalid operator")
 
        Calculate_again=input("Do you want to calculate again?(Yes/No)")
        if Calculate_again.lower()=="Yes":
            calculate()
        elif Calculate_again.lower()=="no":
            break        
            
   

        



