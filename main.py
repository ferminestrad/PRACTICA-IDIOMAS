from numpy import zeros
import numpy as np 
import matplotlib.pyplot as plt
def remove_upper(texto):
    acentos={'À':['A'],'Ä':['A'],'Â':['A'],'Á':['A'],'Ç':['C'],'É':['E'],'Ë':['E'],'Ê':['E'],'È':'E','Ì':'I','Í':'I','Ò':'O','Ó':'O','Ö':'O','Ô':'O','Ù':'U','Û':'U','Ü':'U','Ú':'U'}
    letras="ÀÄÂÁÇÉÈËÊÌÍÒÓÖÙÛÜÚÔ"
    otrotexto=""
    for x in texto:
        alpha=""
        x=x.upper()
        for i in x:
            if i.isalpha():
               alpha+=i
        for x in alpha:
            if x in letras:
                otrotexto+=acentos[x][0]
            else:
                otrotexto+=str(x)
    return otrotexto

def contalpha(otrotexto):
    alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cont=dict.fromkeys(alfabeto,0)
    for x in otrotexto:
        if x not in cont:
            cont[x]=1
        elif x in cont:
            cont[x]+=1
        
    return cont
def grafic(idioma,dicc,y):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = np.arange(len(alpha))
    width = 0.35
    fig, ax=plt.subplots()
    if y==0:
      ax.bar(x - width/2, dicc, width, label='% letras, texto', color=["yellow"])
      ax.bar(x + width/2, idioma, width, label='% letras, idioma Español',color=["red"])
      ax.set_ylabel('%')
      ax.set_title('Porcentajes del alfabeto del texto e idioma')
      ax.set_xticks(x, alpha)
      ax.legend()
      fig.tight_layout()
      plt.show()
    elif y==1:
      ax.bar(x - width/2, dicc, width, label='% letras, texto', color=["red"])
      ax.bar(x + width/2, idioma, width, label='% letras, idioma Inglés',color=["blue"])
      ax.set_ylabel('%')
      ax.set_title('Porcentajes del alfabeto del texto e idioma')
      ax.set_xticks(x, alpha)
      ax.legend()
      fig.tight_layout()
      plt.show()
    
    
    elif y==2:
      ax.bar(x - width/2, dicc, width, label='% letras, texto', color=["cyan"])
      ax.bar(x + width/2, idioma, width, label='% letras, idioma Fránces',color=["red"])
      ax.set_ylabel('%')
      ax.set_title('Porcentajes del alfabeto del texto e idioma')
      ax.set_xticks(x, alpha)
      ax.legend()
      fig.tight_layout()
      plt.show()
      
      
    elif y==3:
      ax.bar(x - width/2, dicc, width, label='% letras, texto', color=["black"])
      ax.bar(x + width/2, idioma, width, label='% letras, idioma Aleman',color=["red"])
      ax.set_ylabel('%')
      ax.set_title('Porcentajes del alfabeto del texto e idioma')
      ax.set_xticks(x, alpha)
      ax.legend()
      fig.tight_layout()
      plt.show()
      
      
    elif y==4:
      ax.bar(x - width/2, dicc, width, label='% letras, texto', color=["red"])
      ax.bar(x + width/2, idioma, width, label='% letras, idioma Italiano',color=["green"])
      ax.set_ylabel('%')
      ax.set_title('Porcentajes del alfabeto del texto e idioma')
      ax.set_xticks(x, alpha)
      ax.legend()
      fig.tight_layout()
      plt.show()
      

def lnguage(porcentajes,li):
    pfinales=zeros(5, dtype=int)
    restas= zeros(5)
    a=0
    for i in porcentajes:
        v=porcentajes.split()
        for x in range(0,5):
            restas[x]=np.abs(float(v[x])-float(li[a]))
        a+=1
        #print(restas)
        menor=restas[x]
        for x in range(0,5):
            if restas[x]<menor:
                menor=restas[x]
            else: 
                menor=menor
        for x in range (0,5):
            if restas[x]==menor:
                pfinales[x]+=1
        porcentajes=abecedario.readline()
    repeticiones=pfinales[0]
    for x in range(0,5):
        if pfinales[x]>repeticiones:
            repeticiones=pfinales[x]
        else:
            repeticiones=repeticiones

    if  repeticiones==pfinales[0]:
        print ("\nEl texto está escrito en Español")
        esp=[11.72,	1.49,	3.87,	4.67,	13.72,	0.69,	1, 1.18,	5.28,	0.52,	0.11,	5.24,	3.08,	6.83,	0.17,	8.44,	2.89,	1.11,	6.41,	7.2,	4.6,	4.55,1.05,	0.04,	0.14,	1.09,	0.47]
        y=0
        grafic(esp,li,y)
    elif repeticiones==pfinales[1]:
        print("\nEl texto está escrito en Inglés")
        eng=[8.34,	1.54,	2.73,	4.14,	12.6,2.03,	1.92,	6.11,	6.71,	0.23,	0.87,	4.24,	2.53,	6.8,0,7.7,	1.66,	0.09,	5.68,	6.11,	9.37,	2.85,	1.06,	2.34,	0.2,	2.04,	0.06]
        y=1
        grafic(eng,li,y)
    elif repeticiones==pfinales[2]:
        print("\nEl texto está escrito en Frances")
        fr=[8.13,	0.93,	3.15,	3.55,	15.1,	0.96,	0.97,	1.08,	6.94,	0.71,	0.16,	5.68,	3.23,	6.42,	0,	5.27,	3.03,	0.89,	6.43,	7.91,	7.11,	6.05,	1.83,	0.04,	0.42,	0.19,	0.21]
        y=2
        grafic(fr,li,y)
    elif repeticiones==pfinales[3]:
        print("\nEl texto está escrito en Alemán")
        al=[5.58,	1.96,	3.16,	4.98,	16.93,	1.49,	3.02,	4.98,	8.02,	0.24,	1.32,	3.6,	2.55,	10.53,	0,	2.24,	0.67,	0.02,	6.89,	6.42,	5.79,	3.83,	0.84,	1.78,	0.05,	0.05,	1.21]
        y=3
        grafic(al,li,y)
    elif repeticiones==pfinales[4]:
        print("\nEl texto está escrito en Italiano")
        ita=[10.85,	1.05,4.3,3.39,11.49,1.01,1.65,1.43,10.18,0,0,5.7,2.87,7.02,0,9.97,2.96,0.45,6.19,5.48,6.97,3.16,1.75,0,0,0,0.85]
        y=4
        grafic(ita,li,y)
  
archivo=open("FRANCES.txt","r")
lineas=archivo.readlines()
a=remove_upper(lineas)
print("Texto limpio: ",a)
dic=contalpha(a)
b=sum(dic.values())#total de letras del texto
print("\nCantidad de letras del abecedario: ",dic)
archivo.close()
for i in dic:
    dic[i]=(dic[i]*100/b)
#print("\nPorcentajes de letras:",dic)
li=dic.values()
li=list(li)
abecedario=open('porcentaje.txt','r')
porcentajes=abecedario.readline()
lnguage(porcentajes,li)
abecedario.close()
  
  
  