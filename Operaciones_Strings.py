
def LeerText():
   
    global frc
    print("\n")
    frc=(input("Ingresa una frase: "))

def contarLetras():
    
    contsig=0
    for i in frc:
         if(i.isalpha()):
            contsig+=1
    print("Número de letras:",contsig)

def LongOriginal():
    global long
    long=len(frc)
    print("La frase tiene una longitud de",long)

def ContaPalabras():
   contpal = 0 
   part=frc.split(" ")
   print (part)
   for j in part:
       if(j.isalpha()):
            contpal+=1
   print("Numero de palabras:",contpal)

def ContaVocales():
    contvoc = 0
    for z in frc:
        if (z in "aeiouAEIOUáéíóúÁÉÍÓÚ"):
            contvoc+=1
    print("El numero de vocales es: ",contvoc)
        
def principal():
    txt=open("mensaje.txt")
    print(txt.read())
    LeerText()
    opc=0
    while (opc!=6):
        print("--------------------------")
        print("|    ¿Qué desea hacer?   |")
        print("|1.- Numero de letras    |")
        print("|2.- Longitud de la frase|")
        print("|3.- Numero de palabras  |")
        print("|4.- Numero de vocales   |")
        print("|5.- Ingresar otro Texto |")
        print("|     6.- Salir          |")
        print("--------------------------")
        opc=int(input(("Ingrese un número: ")))
        if (opc==1):
            contarLetras()    
        elif(opc==2):
            LongOriginal()
        elif(opc==3):
            ContaPalabras()
        elif(opc==4):
            ContaVocales()
        elif(opc==5):
            LeerText()


principal()

