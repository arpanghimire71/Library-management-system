from openpyxl import load_workbook as lw    
import IDgenerator as id
import password as pw

def librarian_register():
    librarian_id=id.generator()
    password=pw.pass_generator()
    librarian_name=input("Enter your name: ")
    wb=lw("C:/Users/Lenovo/OneDrive/Desktop/Library management software/Librarian data.xlsx")
    sheet=wb["Sheet1"]
    sheet.append([librarian_id,librarian_name])