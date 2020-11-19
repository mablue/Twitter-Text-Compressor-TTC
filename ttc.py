# TTC: Twitter text compressing script
# developer: Masoud Azizi
# Email: mablue92@gmail.com
i0="masoud azizi\nJafar AzizI \n amir mohammad AZIZI."
print(i0)

i1=i0.lower()
o0=i1.split(" ")
print(o0)

o2=[o1.capitalize() for o1 in o0]
print(o2)

o3="".join(o2)
print("=======RESULT=======")
print(o3)
