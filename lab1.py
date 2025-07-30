def grade(marks):  #function that takes input as marks and returns the grade
    if int(marks)<=100 and int(marks)>=90:
        return "A"
    elif int(marks)<=89 and int(marks)>=75:
        return "B"
    elif int(marks)<=74 and int(marks)>=60:
        return "C"
    elif int(marks)<=59 and int(marks)>=40:
        return "D"
    elif int(marks)<40:
        return "F"
    
    
marks=input("Enter the marks:")   #Enter the marks
while(marks!="EXIT"):   #run until EXIT
    if(marks.isdecimal()):    #if the string is a number
        if (int(marks)<0 or int(marks)>100):  #out of range condition
            print("Invalid input")
            marks=input("Enter the marks:")
        else:                                #if the marks is in the range
            gd=grade(marks)        # function is called
            print("Your grade is:",gd)
            marks=input("Enter the marks:")
    else:
        print("Invalid input")
        marks=input("Enter the marks:")



    
       
