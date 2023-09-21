class classassignment():
    def Subfields():
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print ("Sub-fields in AI are:")
        for ai in lists:
            print(ai)
            
    #find odd or even       
    def OddEven ():
        number1=int(input("enter the number: "))
        if(number1%2==0):
            print(number1,"is an even number")
        else:
             print(number1,"is an  odd number")
    
    #check elegibility for marriage 
    def Elegible():
        gender=input("Male or Female ")
        age=int(input("enter your age "))
        if(gender=="Male" and age<21):
            print("Your Gender: ",gender)
            print("Your age ",age)
            print("NOT ELIGIBLE")
        elif(gender=="Female" and age<18):
            print("Your Gender: ",gender)
            print("Your age ",age)
            print("NOT ELIGIBLE")
        else:
            print("Your Gender: ",gender)
            print("Your age ",age)
            print(" ELIGIBLE")
            
            
          # check percentage  
    def percentage():
        Total=0
        lists=[98,87,95,95,93]
        totalsubjects=len(lists)
        for marks in lists:
            Total=marks+Total
        print("Subject 1=",lists[0])
        print("Subject 2=",lists[1])
        print("Subject 3=",lists[2])
        print("Subject 4=",lists[3])
        print("Subject 5=",lists[4])
        percentage=float(Total/(totalsubjects*(100)))*100
        print("Total ",Total)
        print("Percentage ",percentage)
        
           
            
            
          #triangle formula  
    def triangle():
        Height=float(input("enter the height: "))
        Breath=float(input("enter the breath: "))
        area= (Height * Breath) *1/2
        print("Area formula: (Height * Breath) *1/2")
        print("Area of triangle : ",area)
        Height1=float(input("Height1:"))
        Height2=float(input("Height2:"))
        breadth=float(input("Breadth:"))
        perimeter=Height1+Height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",perimeter)
           