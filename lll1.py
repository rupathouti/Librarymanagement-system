class Library:
	Librarians=[["Rupa","1234"],["Bhaskar","4321"]]
	Students=[["Sakruti","1111"],["Sukruti","2222"],["Samyukti","3333"],["Ronil","4444"],["Atish","5555"],["Nitesh","6666"],["Avani","7777"],["Varad","9999"]]
	Rack_Book=[["Physics","Einstin","1000"],["Physics","Einstin","1001"],["Physics","Edison","1002"],["Physics","Einstin","1003"],["Physics","Einstin","1004"],["Chemistry","Einstin","2000"],["Chemistry","Thamos","2001"],["Chemistry","Einstin","2002"],["Chemistry","Nobel","2003"],["Chemistry","Einstin","2004"]]

	
	def Change_Login(self,name,pin):
    		if [name,pin] not in lib.Librarians:

        		Librarians=self.Librarians.append([name,pin])
        	
        		print("Update Successfully:",[name,pin])
   		else:
         		print("Librarian already available with same details")

	def Add_Students(self,name,pin):
    		if [name,pin] not in lib.Students:
        		Students=self.Students.append([name,pin])
        		print("Successfully Added with details",[name,pin])
    		else:
         		print("Students already available with details")
 
	def Delete_Students(self,name,pin):
    		if [name,pin] in lib.Students:
       			Students=self.Students.remove([name,pin])
        		print("Successfully deleted details",[name,pin])
    		else:
        		print("No students available with details")  
	
	def Details_Books(self):
    		print("--------------------------------------------------")
    		print("Book name"," ","Author Name"," ","Book ID")
    		print("--------------------------------------------------")

    		for i in range(len(lib.Rack_Book)):
        		print(lib.Rack_Book[i][0],lib.Rack_Book[i][1],lib.Rack_Book[i][2])
        		print("___________________________________________________")

    		print("\nNo of avaliable Books are:",len(lib.Rack_Book))

	def Details_Students(self):
    		print("-------------------------------")
    		print("Sudent name"," ","R.No")
    		print("-------------------------------")

    		for i in range(len(lib.Students)):
        		print(lib.Students[i][0],lib.Students[i][1])
        		print("_______________________________")
    		print("\nNo of Students are:",len(lib.Students))
	
	def Details_Librarians(self):
    		print("-------------------------------")
    		print("Librarian name"," ","Pin")
    		print("-------------------------------")

    		for i in range(len(lib.Librarians)):
        		print(lib.Librarians[i][0],lib.Librarians[i][1])
        		print("_______________________________")
    		print("No of Librarians are:",len(lib.Librarians))


	def Update_Book(self,name,author,Bid):
    		if [name,author,Bid] not in lib.Rack_Book:

        		Rack_Book=self.Rack_Book.append([name,author,Bid])
        	
        		print("Update Successfully:",[name,author,Bid])
   		else:
         		print("Book already available with same details")

lib=Library();
print("Welcome to Library")
print("Select your Option\n 1:Librarian Login\n 2:Student Login\n 3:Exit")

opt1=int(input("Please Enter your option:"))

if opt1==1:
    i=1
    while (i<4):
        usrlib=raw_input("Please Enter your Name:")
        pinlib=raw_input("Please Enter your Login PIN:")

        if [usrlib,pinlib] in lib.Librarians:
            print("Access Granted")
            
            while(True):
                print("Select your Option\n 0:Change Username or Password\n 1:Add Books\n 2:Books Details\n 3:Add Students\n 4:Remove Students\n 5:Students details\n 6:Librarian details\n 7.Exit or Back\n 8.Quit")
                opt2=int(raw_input("Please Enter your option:"))
                if opt2==0:
                    usrlib1=raw_input("Please Enter User Name to change:")
                    pinlib2=raw_input("Please Enter Login PIN to change:")
                    lib.Change_Login(usrlib1,pinlib2)
		    print(Librarians)

                elif opt2==1:
                    name=raw_input("Please Enter your Book Name:")
                    author=raw_input("Please Enter your Book Author:")
                    Bid=raw_input("Please Enter your Book Id:")
                    lib.Update_Book(name.capitalize(),author.capitalize(),Bid)

                elif opt2==2:
                    lib.Details_Books()

                elif opt2==3:
                    name=raw_input("Please Enter Student Name:")
                    pin=raw_input("Please Enter Student R.No:")
                    lib.Add_Students(name.capitalize(),pin)
                elif opt2==4:
                    name=raw_input("Please Enter Student Name:")
                    pin=raw_input("Please Enter Student R.No:")
                    lib.Delete_Students(name.capitalize(),pin)    
                elif opt2==5:
                    lib.Details_Students()
		elif opt2==6:
                    lib.Details_Librarians()
                elif opt2==7:    
                    print("Back to Menu")
                elif opt2==8:    
                    exit()    
                else:
                    print("Wrong input")
                    break

        else:
            print("Access Denied \nUser name or PIN Entered wrong")
            print("You have more",(3-i),"attempts")
            i+=1
            if i==4:
                print("Failed login within 3 attempts")
