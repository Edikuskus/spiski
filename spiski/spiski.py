text=input("Sisesta tekst: ")
text_list=list(text)
k=len(text_list)
if text.isdigit():
    for t in range(k):
        num=int(text_list[t])
        text_list.pop(t)
        text_list.insert(t,num)


    summa=0
    for e in text_list:
        summa+=e
    print("summa: ", summa )
print(text_list)
e=input("Element: ") #str
try:
    if e.isalpha():
        indeks=text_list.index(e)
    else:
        indeks=text_list.index(int(e))
    print("Element: {0} on {1} positsioonil".format(e,indeks))
except :
    print("Element puudub")


import string
vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
konsonanti="qwrtpsdfghklzxcvbnmj"
markid=string.punctuation
v=k=m=t=0
while True:
    tekst=input("Sisesta sõna või lause: ")
    if tekst.isdigit():
        break
    else:
        tekst_l=list(tekst)
        for e in tekst_l:
            if e.lower() in vokaali:
                v+=1
            elif e.lower() in konsonanti:
                k+=1
            elif e.lower() in markid:
                m+=1
            elif e.lower()==" ":
                t+=1
    print("Vokaali:", v)
    print("konsonanti:",k)



##2
#l=[11,2,3,4,5,6,2,3,9,2,2,2,2]
#l_set=set(l)
#print(l_set)
#for e in l_set:
#    print(e*"*")


indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa" , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa" ,"Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]

while True:
    try:
        index=int(input("privet, napishi svoi indeks "))  #eto ciframi 123
        if len(str(index))==5: #eto v skobkah "123"
               break
    except:
        print("ne pravilno")
print("analiz indexa")
index_list=list(str(index))
s1=int(index_list[0]) #1 Tallinn c indexa 0
print("index {0} on {1} piirkonnas".format(index,indexid[s1-1]))
        


#5

from random import *

kokku=randint(2,20)
num_list=[]
for i in range(kokku):
    num_list.append(randint(-100,100))
print(num_list)
print()
while True:
    try:
        kogus=int(input("skolko pozitsii ?"))
        if kogus<=kokku/2:
            break
    except:
        print("poprobui eshe raz")

for i in range (0,kogus,1):
    X_tmp= num_list[i]
    print(str(i)," ", str(num_list[i]),"  ",str(num_list[(len(num_list)-i)-1]),"\n")
    print(X_tmp, "\n")

    num_list[i]= num_list[(len(num_list)-i)-1]
    num_list[(len(num_list)-i)-1]= X_tmp
print("\n", num_list)


#6
kokku=randint(2,20)
print("itog v poradke ",kokku,"element")
num_list=[]
for i in range(kokku):
    num_list.append(round(random()*1000,2))
print(num_list)
max_=max(num_list)
n=num_list.index(max_)
print("\t",max_,"pozichia:",n+1)
num_list.pop(n)
max_=max_/len(num_list)
num_list.insert(n,max_)
print(num_list)







