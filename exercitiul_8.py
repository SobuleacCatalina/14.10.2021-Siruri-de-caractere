sir="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
sir1=sir
sir2=sir
sir3=sir
for i in range(0,len(sir1)-2,2):
        sir1[i]=chr(ord(sir1[i])+1)
print(sir1)
while (sir2.find("Z")>=0):
    sir2[sir2.find("Z")+1]="A"
print(sir2)
while (sir3.find(" ")>=0):
    sir3[sir3.find(" ")+1]="-"
print(sir3)