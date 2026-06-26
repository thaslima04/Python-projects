students=[]
while True:
     print("STUDENT RECORD SYSTEM")
     print("1.Add student")
     print("2.View student")
     print("3.Search student")
     print("4.Exit")
     choice=input("enter your choice:")
     if choice=="1":
         name=input("enter name:")
         marks=input("enter marks:")
         students.append([name,marks])
         print("student added successfully")
     elif choice=="2":
         if len(students)==0:
             print("no students found")
         else:
             for s in students:
                 print("name:",s[0],"marks:",s[1])
     elif choice=="3":
         name=input("enter student name to search:")
         found=False
         for s in students:
             if s[0]==name:
                 print("found:",s[0],"marks:",s[1])
                 found=True
             else:
                 print("student not found")
     elif choice=="4":
         print("Exit")
         break
     else:
         print("Invalid choice")
