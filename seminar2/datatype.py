a=5
print(a,id(a))
a +=1
print(a,id(a)) #числа не изменяемые,создаются объекты, дается стикер на расположение в памяти динамически

txt ='come to daddy'
print(txt, id(txt))
txt=txt.replace(' ', '_')
print(txt,id(txt))
