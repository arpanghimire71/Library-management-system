import random

# password Generator

symbols=["*","$","@","%","!","?","<",">","&","(",")","+","-","/","_"]

def pass_generator():
    password=""
    for i in range(3):
        sym=random.choice(symbols)
        num=random.randint(0,9)
        num=str(num)
        capital_letter=random.randint(65,90)
        small_letter=random.randint(97,122)
        password=num+chr(capital_letter)+sym+chr(small_letter)+password
    chars=list(password)  
    random.shuffle(chars) 
    shuffled_text=''.join(chars) 
    return shuffled_text

if __name__=="__main__":
    pass_generator()

      

 
    

