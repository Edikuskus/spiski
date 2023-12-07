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
konsonanti="qwrtpsdfghklzxcvbnm"
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







