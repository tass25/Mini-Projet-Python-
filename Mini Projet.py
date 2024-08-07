import json
from multiprocessing.sharedctypes import Value
from operator import mod
import os 
from time import sleep
from datetime import datetime
from wsgiref.handlers import CGIHandler
import numpy as np
import matplotlib.pyplot as plt



def check():                    #======= Creating Folder + File .json ==========  
    path = "C:\MiniProjet"         

    if os.path.isdir(path) == True :        
        print("Available Directory")
    else : 
        try : 
            os.mkdir(path)

        except OSError:
            print("Creation of the directory %s failed" % path)

        else : 
            print("Succefully created the directory %s" % path)

    if os.path.isfile((path+'\data.json')and(path+'\car.json')and(path+'\date.json')):       #Check if file path Exist or No 
        print("File Ready ")

    else :          #Creating txt File into custom path
        print("File 404 Not Found ")
        sleep(1)
        print(" Creating ...")
        sleep(2)

        with open (path+'\data.json','x') as dataFile:

            print("File Ready to Collect Data ")
            print("Check Here",path,"To Find Your Folder")
        with open (path+'\car.json','x') as dataFile:

            print("File Ready to Collect Data ")
            print("Check Here",path,"To Find Your Folder")

        with open (path+'\date.json','x') as dataFile:

            print("File Ready to Collect Data ")
            print("Check Here",path,"To Find Your Folder")


    sleep(3)

    os.system('cls')


check()

        #============================ End Of Check Function ===================================


condidat = {
"CIN":'',
"PermisType":'',
"SCode" : {
        "Num":'',
        "date":'',
        "heure":'',
        "ing":''},
"SCond" : {
        "Num":'',
        "date":'',
        "heure":'',
        "véhicule":'',
        "ing":''}
}


flotte = {
    "Type":'',
    "Mat":'',
    "DMS":'',
    "KMT":'',
    "KMRS":''
}

Seance = {
    "Valid Date":'',
    "Invalid Date":''
}
def proj():
 choix = int(input("""1- La Gestion des Condidats \n
2- La Gestion des Véhicules \n
3- La Gestion et la Planification des séances \n
Votre Choix:\n
"""))

 while (choix > 3 or choix < 1):
    print("invalid Option")             #Choix Test
    break

 if choix == 1 : 
    CRUD = int(input("""    1- ajouter \n
    2- Modifier \n
    3- Supprimer \n
    4- Recherche
    """))
    while (CRUD > 4 or CRUD < 1):
        print("Invalid Option")             #CRUD Test
        break

    if CRUD == 1 : 
        CIN = int(input("Donner le Num CIN : "))

        while (CIN > 99999999 or CIN < 10000000):
                print("Invalid CIN Number")
                break
        else : 
                condidat.update({"CIN": CIN})

        PT = input("Type De Permis : ")
        
        if PT.upper() == 'A' or PT.upper() =='B' or PT.upper() == 'C':
            condidat.update({"PermisType":PT})
        else: 
            print(" Invalid")
       
        print(" =================== Code Infos ===================\n")

        NumSC = int(input("Donner Le Num de Séance de Code : "))

        while (NumSC < 0):
            print("Invalid Number")
            break
        else : 
            condidat["SCode"].update({"Num":NumSC})

        Date = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(Date, format)
            condidat["SCode"].update({"date":Date})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")

        heure = int(input("Donner nombre d'heure : "))

        while (heure < 0):
            print("invalid number ")
        else : 
            condidat["SCode"].update({"heure":heure})

        ing = input("Donner le nom d ing : ")

        while (ing ==''):
            print("Blank Input")
        else: 
            condidat["SCode"].update({"ing":ing})

        print(" =================== Conduite Infos ===================\n")
        
        NumSCo = int(input("Donner Le Num de Séance de Conduite : "))

        while (NumSCo < 0):
            print("Invalid Number")
            break
        else: 
            condidat["SCond"].update({"Num":NumSCo})

        DateC = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(DateC, format)
            condidat["SCond"].update({"date":DateC})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")
        

        heureC = int(input("Donner nb heure : "))
        while (heureC < 0):
            print("invalid number ")
            break
        else : 
            condidat["SCond"].update({"heure":heureC})

        car = input("Nom de véhicule : ")
        condidat["SCond"].update({"véhicule":car})

        ingC = input("Donner le nom d ing : ")
        while (ingC ==''):
            print("Blank Input")
            break
        else: 
            condidat["SCond"].update({"ing":ingC})


        if (PT.upper() == 'A'):
            prixTot = (((15*0.02)+15)* heure) + (((15*0.04)+15)* heureC)
            condidat["prixTotal"] = (str(prixTot)+'DT')
        
        elif (PT.upper() == 'B'):
            prixTot = (((15*0.03)+15)* heure) + (((15*0.06)+15)* heureC)
            condidat["prixTotal"] = (str(prixTot)+'DT')

        elif (PT.upper() == 'C'):
            prixTot = (((15*0.05)+15)* heure) + (((15*0.08)+15)* heureC)
            condidat["prixTotal"] = (str(prixTot)+'DT')

        PP = int(input("Donner le prix payé : "))
        condidat["PrixPaye"] = (str(PP)+'DT')

        PR = prixTot - PP 
        condidat["PrixRester"] =(str(PR)+'DT')

        dataFile = open('C:\MiniProjet\data.json','a')
        json.dump(condidat,dataFile)
        
    if CRUD == 2 : 
        openfile = open('C:\MiniProjet\data.json','r')
        dataLoad = json.load(openfile)
        openfile.close()
        print(dataLoad)
        CIN = int(input("Donner le Num CIN : "))

        while (CIN > 99999999 or CIN < 10000000):
                print("Invalid CIN Number")
                break
        else : 
                dataLoad.update({"CIN": CIN})

        
        PT = input("Type De Permis : ")
        
        if PT.upper() == 'A' or PT.upper() =='B' or PT.upper() == 'C':
            dataLoad.update({"PermisType":PT})
        else: 
            print(" Invalid")
       
        print(" =================== Code Infos ===================\n")

        NumSC = int(input("Donner Le Num de Séance de Code : "))

        while (NumSC < 0):
            print("Invalid Number")
            break
        else : 
            dataLoad["SCode"].update({"Num":NumSC})

        Date = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(Date, format)
            dataLoad["SCode"].update({"date":Date})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")

        heure = int(input("Donner nombre d'heure : "))

        while (heure < 0):
            print("invalid number ")
        else : 
            dataLoad["SCode"].update({"heure":heure})

        ing = input("Donner le nom d ing : ")

        while (ing ==''):
            print("Blank Input")
        else: 
            dataLoad["SCode"].update({"ing":ing})

        print(" =================== Conduite Infos ===================\n")
        
        NumSCo = int(input("Donner Le Num de Séance de Conduite : "))

        while (NumSCo < 0):
            print("Invalid Number")
            break
        else: 
            dataLoad["SCond"].update({"Num":NumSCo})

        DateC = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(DateC, format)
            dataLoad["SCond"].update({"date":DateC})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")
        

        heureC = int(input("Donner nb heure : "))
        while (heureC < 0):
            print("invalid number ")
            break
        else : 
            dataLoad["SCond"].update({"heure":heureC})

        car = input("Nom de véhicule : ")
        dataLoad["SCond"].update({"véhicule":car})

        ingC = input("Donner le nom d ing : ")
        while (ingC ==''):
            print("Blank Input")
            break
        else: 
            dataLoad["SCond"].update({"ing":ingC})


        if (PT.upper() == 'A'):
            prixTot = (((15*0.02)+15)* heure) + (((15*0.04)+15)* heureC)
            dataLoad["prixTotal"] = (str(prixTot)+'DT')
        
        elif (PT.upper() == 'B'):
            prixTot = (((15*0.03)+15)* heure) + (((15*0.06)+15)* heureC)
            dataLoad["prixTotal"] = (str(prixTot)+'DT')

        elif (PT.upper() == 'C'):
            prixTot = (((15*0.05)+15)* heure) + (((15*0.08)+15)* heureC)
            dataLoad["prixTotal"] = (str(prixTot)+'DT')

        PP = int(input("Donner le prix payé : "))
        dataLoad["PrixPaye"] = (str(PP)+'DT')

        PR = prixTot - PP 
        dataLoad["PrixRester"] =(str(PR)+'DT')
        dataFile = open('C:\MiniProjet\data.json','w')
        json.dump(dataLoad,dataFile)
    if CRUD ==3:
        dataLoad = json.load(open('C:\MiniProjet\data.json'))
        supps = input('donner le Nom a supp ')
        if dataLoad.keys() == supps:
            dataLoad.pop(supps)
        dataFile = open('C:\MiniProjet\data.json','w')
        json.dump(dataLoad,dataFile)


 if choix == 2 : #vehi
    CRUD = int(input("""    1- ajouter \n
    2- Modifier \n
    3- Supprimer \n
    4- Recherche
    """))
    while(CRUD > 4 or CRUD < 1):
        print("Invalid Option")             #CRUD Test
        break 
        
    if CRUD ==1 : #ajoutv
        type = input("type de voiture")
        flotte.update({"Type":type})
        
        mat = input('donner le matricule de voiture ')
        flotte.update({'Mat':mat})

        Date = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(Date, format)
            flotte.update({"DMS":Date})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")
        
        kmt = int(input("Donner le KM Total"))
        flotte.update({"KMT":kmt})

        kmrs = int(input("Dooner le KMRS"))
        flotte.update({"KMRS":kmrs})
        
        dataFile = open('C:\MiniProjet\car.json','a')
        json.dump(flotte,dataFile)

    if CRUD == 2 : #modifv
        openfile = open('C:\MiniProjet\car.json','r')
        dataLoad = json.load(openfile)
        openfile.close()
        
        type = input("type de voiture")
        dataLoad.update({"Type":type})
        
        mat = input('donner le matricule de voiture ')
        dataLoad.update({'Mat':mat})

        Date = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"

        try:
            datetime.strptime(Date, format)
            dataLoad.update({"DMS":Date})
        except ValueError:
            print("This is the incorrect date string format. It should be JJ-MM-AAAA")
        
        kmt = int(input("Donner le KM Total"))
        dataLoad.update({"KMT":kmt})

        kmrs = int(input("Dooner le KMRS"))
        dataLoad.update({"KMRS":kmrs})
        
        dataFile = open('C:\MiniProjet\car.json','w')
        json.dump(dataLoad,dataFile)
        

    if CRUD == 3 :#supp v
        dataLoad = json.load(open('C:\MiniProjet\car.json'))
        supps = input('donner le Value a supp ')
        if dataLoad.keys() == supps:
            dataLoad.pop(supps)
        dataFile = open('C:\MiniProjet\car.json','w')
        json.dump(dataLoad,dataFile)


 if choix == 3 : #planification
    CRUD = int(input("""    1- ajouter \n
    
    2- Supprimer \n
    
    """))
    while (CRUD > 2 or CRUD < 1):
        print("Invalid Option")             #CRUD Test
        break
        
    if CRUD == 1 : 
        Date = input('Enter date (JJ-MM-AAAA) : ')
        format = "%d-%m-%Y"
        datetime.strptime(Date, format)
        ans = int(input("""    1- Valid \n
        2- Invalid \n
        """))
        if ans == 1 : 
            Seance.update({"Valid Date":Date})
        elif ans == 2 :
            Seance.update({"Invalid Date":Date})
        
        dataFile = open('C:\MiniProjet\date.json','w')
        json.dump(Seance,dataFile)

    if CRUD == 2: 
        dataLoad = json.load(open('C:\MiniProjet\date.json'))
        supps = input('donner le Value a supp ')
        if dataLoad.keys() == supps:
            dataLoad.pop(supps)
        dataFile = open('C:\MiniProjet\date.json','w')
        json.dump(dataLoad,dataFile)
def courbe():
    datafile = open('C:\MiniProjet\car.json','r')
    dataload = json.load(datafile)
    datafile.close()
    x=np.empty(0,int)
    y=np.empty(0,int)
    for i in dataload:
     x=int(np.append(x,dataload['KMT']))
     y=int(np.append(y,dataload['KMRS']))
    plt.plot(x, y)
    plt.show()
def menu1():
    print("\t\t\t\t ******                              **                              ")
    print("\t\t\t\t/*////**                            //                               ")
    print("\t\t\t\t/*   /**     ******    *******       **    ******    **   **   ******")
    print("\t\t\t\t/******     **////**  //**///**     /**   **////**  /**  /**  //**//*")
    print("\t\t\t\t/*//// **  /**   /**   /**  /**     /**  /**   /**  /**  /**   /** / ")
    print("\t\t\t\t/*    /**  /**   /**   /**  /**   **/**  /**   /**  /**  /**   /**   ")
    print("\t\t\t\t/*******   //******    ***  /**  //***   //******   //******  /***   ")
    print("\t\t\t\t///////     //////    ///   //    ///     //////     //////   ///    ")
    print("\t\t\t\t  ╔═══════════════════════════════════════╗\n")
    print ("\t\t\t\t  ♠  Nom et Prénom : Tesnime  Ellabou     ♠ \n")
    print ("\t\t\t\t  ║                                       ║\n")
    print ("\t\t\t\t  ♠         Classe : CPI 1 B              ♠ \n")
    print ("\t\t\t\t  ║                                       ║ \n")
    print ("\t\t\t\t  ♠  année universitaire : 2021 - 2022    ♠\n")
    print ("\t\t\t\t  ║                                       ║\n ")
    print ("\t\t\t\t  ♠ Faculté  des  Sciences  du  Bizerte   ♠ \n")
    print ("\t\t\t\t  ╚═══════════════════════════════════════╝  \n")
    print("\n\n")
    print("\t\t\t\t         GESTION  D'AUTO ECOLE   ")
    print("\t\t\t\t         *********************** ")
menu1()
sleep(6)
os.system('cls')
while True :
    proj()
    print(condidat)
    #print(flotte) pour visualiser les cars

