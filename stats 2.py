import csv
import pandas
import pickle
import math
#%%
lignes = []
lignesdate2 = []

#%%


lignesdate = []

n=1   
while n <= 5:    
    a ="C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/novembre/FTLIV_IRIS/export("+str(n)+").csv"
    r = pandas.read_csv(a, delimiter = ";", usecols =[0,1])
    lignesdate = lignesdate + [r.values.tolist()]
    n += 1



#%%


def colisrecup(excel):
    x = pandas.read_csv(excel, delimiter= ";", usecols =[0,2,3,4])
    lignes.append(x.values.tolist())
    return lignes



#%%

colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675094972749.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095113695.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095299560.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095475771.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095594307.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095812896.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675095974396.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675096167705.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675096269807.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675096543957.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675096738495.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675097030506.csv")
colisrecup("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/export_1675097318180.csv")
#%%

print(len(lignes))
print(len(lignes[0]))
print(len(lignes[1]))
print(len(lignes[2]))
print(len(lignes[3]))
print(len(lignes[4]))
print(len(lignes[5]))
print(len(lignes[6]))
print(len(lignes[7]))
print(len(lignes[8]))
print(len(lignes[9]))
print(len(lignes[10]))
print(len(lignes[11]))
print(len(lignes[12]))


#%%
a=0
for i in range(13):
    a+= len(lignes[i])
    
print(a)
#%%
lignes2 = lignes.copy()

#%%
r = []
for i in range(len(lignes)):
    lignesdate2.append([])
#%%
print(lignesdate2)
#%%
for i in range(len(lignes)):
    for k in range(len(lignes[i])):
        lignesdate2[i].append(lignes[i][k][0].split('"'))
        r.append([lignes[i][k][0],lignesdate2[i][k][1]])
        lignes[i][k][0] = lignesdate2[i][k][1]
#%%
print(lignes[5][390][0])
print(lignesdate2[5][390][1])

# print(r)
#%%


print(lignes[1][2])

#%%



with open("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/balec.txt","w") as log:
    log.write(str(lignes))
    
    
#%%
listefin = []


for i in range(len(lignesdate)):
    for j in range(len(lignesdate[i])):
        for k in range(len(lignes)):
            for r in range(len(lignes[k])):
                if lignes[k][r][0] == lignesdate[i][j][0]:
                    listefin.append([lignes[k][r],lignesdate[i][0][1]])
                
                
              
                
#%%          


listefin2 = []

for elt in listefin:
    if elt not in listefin2:
        listefin2.append(elt)
    
    

print(len(listefin2))
      
 




#%%
with open("C:/Users/erwan/OneDrive/Bureau/CPPG/Cours 2A CPPG/Projet 2A/Données Grenoble/décembre/FTLIV_IRIS/balec.txt","w") as log:
    log.write(str(listefin2))
#%%
def colishn1(date):
    nj =[]
    for l in range(len(listefin2)):
        if listefin2[l][1] == date:
            nj.append((date,listefin2[l][0][0]))
    return  nj
#%%

print(colishn1('2022-12-02 00:00'))


#%%
nombrej = [len(colishn1('2022-12-02 00:00')),len(colishn1('2022-12-03 00:00')),len(colishn1('2022-12-05 00:00')),len(colishn1('2022-12-06 00:00')),len(colishn1('2022-12-07 00:00')),len(colishn1('2022-12-08 00:00')),len(colishn1('2022-12-09 00:00')),len(colishn1('2022-12-10 00:00'))]
print(nombrej)   


#%%
def colishn(date):
    R =[]
    for l in range(len(listefin2)):
        if listefin2[l][0][1]*listefin2[l][0][2]*listefin2[l][0][3] != 0:
            if listefin2[l][1] == date:
                if listefin2[l][0][1]*listefin2[l][0][2]*listefin2[l][0][3] > 94500 or max(listefin2[l][0][1],listefin2[l][0][2],listefin2[l][0][3])>60 or min(listefin2[l][0][1],listefin2[l][0][2],listefin2[l][0][3])>35 or ((listefin2[l][0][1]*listefin2[l][0][2]*listefin2[l][0][3])/(max(listefin2[l][0][1],listefin2[l][0][2],listefin2[l][0][3])*min(listefin2[l][0][1],listefin2[l][0][2],listefin2[l][0][3]))) > 45:
                    R.append([listefin2[l][0][0],listefin2[l][1]])
    return(R)
nombrecolis = [len(colishn('2022-12-02 00:00')),len(colishn('2022-12-03 00:00')),len(colishn('2022-12-05 00:00')),len(colishn('2022-12-06 00:00')),len(colishn('2022-12-07 00:00')),len(colishn('2022-12-08 00:00')),len(colishn('2022-12-09 00:00')),len(colishn('2022-12-10 00:00'))]
print(nombrecolis)

#%%


print(len(listefin2))
print(a)


#%%
def dates():
    differentesdates = []
    for l in range(len(listefin2)):
        if not listefin2[l][1] in differentesdates:
            differentesdates.append(listefin2[l][1])
                
    return differentesdates

print(dates())

#%%
pourcentage = []
for r in range(len(nombrecolis)):
    pourcentage.append((nombrecolis[r]*100)/nombrej[r])
#%%
print(pourcentage)
print((sum(pourcentage)/len(pourcentage)))