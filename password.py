import os
import glob
import re
import random


base_dir = os.getcwd()
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    
def messages(option,data,fileDir):    
    if (os.name == "ce" or os.name == "nt" or os.name == "dos"):
        fileDir = fileDir.replace("\\","/")
    
    if(option == "endOne"):
        print("The number of passwords checked is: {}".format(data))
        print(f"The feedback (output) can be found in the file {fileDir}/Users-Pwds-Chked")
        

def passwordValitator(password):
    tamano = len(password)
    abc = 0
    abc_mayus = 0
    num = 0
    caraspecial = 0
    if(tamano>=8):
        for i in range(33, 127):
            if(i >= 97 and i <= 122):
                abc = abc + len(re.findall(chr(i), password))
            elif(i >= 65 and i <= 90):
                abc_mayus = abc_mayus + len(re.findall(chr(i), password))
            elif(i >= 48 and i <= 57):
                num = num + len(re.findall(chr(i), password))
            elif(i in [33,35,36,37,38,42,43,45,61,63,64,94,95]): 
                val = ""
                if(i==94 and i==94):
                    val = chr(i)                    
                else:
                    val = "["+chr(i)+"]"
                caraspecial = caraspecial + len(re.findall(val, password))
                
        if(tamano>=11 and abc_mayus>=1 and num>=1 and caraspecial>=1):
            return "STRONG"
        if((abc_mayus>=1 and num>=1) or (caraspecial>=1 and abc_mayus>=1) or (num>=1 and caraspecial>=1)):
            return "MODERATE"
        else:
           return "POOR"
    else:
        return "POOR" 
def passwordGenerator():    
    abc = []
    for i in range(33, 127):
        if((i >= 97 and i <= 122) or (i >= 65 and i <= 90) or (i >= 48 and i <= 57) or (i in [33,35,36,37,38,42,43,45,61,63,64,94,95]) or (i==94 and i==94)):
            abc.append(chr(i))    
    password = ''.join(random.sample(abc, random.randint(11, 20)))    
    return password
    
def gettxt_file(directory):
    split_dir = directory.split(".")  
    print(directory)  
    if(len(split_dir) == 2):
        filepath = glob.glob(directory, recursive=True)
        print(filepath)
        if (split_dir[1] == "txt" and filepath != []):                         
            return directory
        else:                                
            file = open(split_dir[0]+".txt", "a")
            file.close()
            return split_dir[0]+".txt"
    else:             
        filevalid= split_dir[0] + ".txt"
        file = open(filevalid, "a")
        file. close()
        return filevalid
   
        
def fileValitator(tipe):
     while True:
        borrarPantalla()
        entrada = input(f"""
        would you like to save the {tipe} file elsewhere?

(press enter to use the default address)
>""")
        
        try:
            if(entrada == ""):                
                return base_dir+'/Users-Pwds.txt'
            else:
                split_entrada = entrada.split(".")                
                ruta = str(split_entrada[0].replace(r"\\","/"))                
                ruta = ruta.split("\\")                        
                lim = len(ruta)
                if(len(split_entrada)>=2):
                    delete_let = 1+len(ruta[lim-1]) +1+ len(split_entrada[1])
                    ruta_corregida = entrada[0:-delete_let]                    
                else:
                    ruta_corregida = str(split_entrada[0]+".txt")
                    
                if(os.path.exists(ruta_corregida)):                
                    base_text_dir = gettxt_file(entrada)
                    return base_text_dir
                else:
                    print ("entrada incorrecta")         
        except ValueError:
            print ("entrada incorrecta")   

def optionOne(fileDir):
    datos = []
    file = open(fileDir, "r")
    lineas = file.readlines()
    for linea in lineas:
        dt = linea.split(",")
        print(dt)
        if(len(dt)==2):  
            datos.append([dt[0],dt[1].rstrip('\n'),passwordValitator(dt[1])])        
    file.close()
    return datos
def optionTwo():
    user = ""
    while True:
        if(user == ""):
            user = input(f"""
        Enter the username: (maximun 20 chars)
        
>""")
            if (len(user) <= 20 and len(user) >= 1):
                password = passwordGenerator()
                print(f"""
        Username: {user}
        Password: {password}
            """)
        else:
            password = passwordGenerator()
            print(f"""
        Username: {user}
        Password: {password}
            """)             
            
        response = input("""
        Would you like save? (Y or N)
>""")
        if(response in ["Y","y"]):
            return True , [user,password]
        elif(response in ["N","n"]):
            reafirm = input(f"""
        Would you like to generated a different password for this user? (Y or N)                            
>""")
            if(reafirm in ["Y","y"]):
                continue
            elif(reafirm in ["N","n"]):
            
                return False
            elif(reafirm not in ["Y","y","N","n"]):
                print("answer yes (y) or no (n)")
            
        elif(response not in ["Y","y","N","n"]):
            print("answer yes (y) or no (n)")



def saveData(data,tipe):
    try:
        if(tipe == "input"):
            file = open(base_dir+'/Users-Pwds-Chked.txt', "w")
            for linea in data:
                file.write(linea[0]+","+linea[1]+","+linea[2]+"\n")                                 
            file.close()
            return True
        elif(tipe == "output"):
            file = open(base_dir+'/Users-Pwds-Chked.txt', "a")            
            file.write(data[0]+","+data[1]+"\n")                                 
            file.close()
            return True
    except ValueError:
            print ("error")
            return False

        
        
def init():
    data = []
    fileDir = ""
    option = ""
    while True:
        borrarPantalla()
        messages(option,len(data),base_dir)
        print(f"""
        Title of your program
            1)
            2)
            default output > {base_dir}
            3)exit
        """)
        entrada = input(">")
        try:
            entrada = int(entrada)
            if(entrada == 1):
                
                filevalid = fileValitator("input")
                data = optionOne(filevalid)
                saveData(data,"input",)
                option = "endOne"
            elif(entrada == 2):
                one,two = optionTwo()               
                if(one):
                    fileDir = fileValitator("output")
                    saveData(two,"output")                  
                    
            elif(entrada == 3):
                borrarPantalla()
                print ("The program is courtesy of: ")
                exit()
            else:
                print ("La entrada es incorrecta: escribe 1 ( para  ) o 2 ( para  )")         
        except ValueError:
            print ("La entrada es incorrecta: escribe 1 ( para  ) o 2 ( para  )")

init()

