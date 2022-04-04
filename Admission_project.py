print ("\nJASPER PRIMARY SCHOOL\n")
class intro:
    print("Welcome to our school\n")
    print("Please choose any of the value below to continue:\n")
    
    def __init__ (self,Name="", Age="", Gender="", Fathername="", Contactnumber="", Previousschool="", b=0):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Fathername=Fathername
        self.Contactnumber=Contactnumber
        self.Previousschool=Previousschool
        self.b=b
        
    def result (self):
        self.Name=input("Name: ")
        self.Age=input("Age: ")
        self.Gender=input("Gender: ")
        self.Fathername=input("Father's Name: ")
        self.Contactnumber=input("Contact Number: ")
        self.Previousschool=input("Name of Previous School: ")
        print("\nYour Application is Submitted Successfully\n")
        print("You will be contacted shortly 😃😃😃\n")
    def standard(self):
        while(1):
            a=int(input("Class = "))
            if a==1:
                print("Per Term Fee is Rs:1800/-", "Totally there are 3 Terms per year.")
                self.b=1800*3
            if a==2:
                print("Per Term Fee is Rs:2800/-", "Totally there are 3 Terms per year.")    
                self.b=2800*3
            if a==3:
                print("Per Term Fee is Rs:3800/-", "Totally there are 3 Terms per year.")
                self.b=3800*3
            if a==4:
                print("Per Term Fee is Rs:4800/-", "Totally there are 3 Terms per year.")
                self.b=4800*3
            if a==5:
                print("Per Term Fee is Rs:5800/-", "Totally there are 3 Terms per year.")
                self.b=5800*3
            if a>5:
                self.b=("\nSorry for the inconvenience as we only taking classes upto fifth standard, your input is invalid\n")
                print(">>>>>Redirecting you to Home Page>>>>>>\n")
                break
            else:
                print( "So the total fee per year =",self.b,"\n")
                break

                
    def contact(self):
        print ("CONTACT DETAILS")
        print ("\nJASPER MATRICULATION SCHOOL")
        print ("No.110/23, Pachaiyappan Street")
        print ("KK Nagar")
        print ("Chennai - 600023")

def main():
    c=intro()
    while(1):
        print ("For Admission Enter 1")
        print ("For Fees Enquiry Enter 2")
        print ("For Contact Enter 3")
        print ("Exit 4\n")
        d= int(input("Enter the value: "))
        if (d==1):
            c.result()
        if (d==2):
            c.standard()
        if (d==3):
            c.contact()
        if (d==4):
            print("Thank you!!!")
            quit()
               

main()
