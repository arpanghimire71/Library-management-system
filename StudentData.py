from openpyxl import load_workbook as lw
import password as pw
import IDgenerator as id

def load_students():
        global status
        status="Logged in"
        student_id=id.id_generator()
        login_password=pw.pass_generator()
        student_name=input("Enter your name: ")
        wb=lw("C:/Users/Lenovo/OneDrive/Desktop/Library management software/Student information.xlsx")
        sheet=wb["Sheet1"]
        sheet.append([student_id,student_name,login_password])
        wb.save("C:/Users/Lenovo/OneDrive/Desktop/Library management software/Student information.xlsx")
        print("Please note down your student ID and password for future login\n")
        print(f"Student ID: {student_id}")
        print(f"Login Password: {login_password}")

def student_login():
     global status 
     status="Logged out"
     entered_id=input("Enter your student   id:")
     entered_password=input("Enter your login pasword:")
     wb=lw("C:/Users/Lenovo/OneDrive/Desktop/Library management software/Student information.xlsx")
     sheet=wb["Sheet1"]
     for row in sheet.iter_rows(min_row=2,values_only=True):
          student_id,student_name,login_password=row
          if entered_id==str(student_id) and entered_password==str(login_password):
               print(f"Welcome {student_name}")
               status="Logged in"
               break
     else:
          print("Invalid student id or password")

def master():
    print("Click 1 to register student data \n Click 2 to login \n Click 3 to exit")
    a= input("Enter your choice: ")
    if a=="1":
        load_students()
        exit()
    if a=="2":
        student_login()
    if a=="3":
        print("Exitted successfully") 
        exit()    
if __name__=="__main__":
     master()

