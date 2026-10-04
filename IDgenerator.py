import random

def id_generator():
    id1=""
    for i in range (3):
        id1=id1+str(random.randint(0,9))
 
    return "S"+id1

if __name__=="__main__":
    id_generator()
