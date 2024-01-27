sayilar=[]
harfler={"A","B","C","D","E","F","G","H","I"}
for i in range(100):
    sayilar.append(str(i))
sayilarset=set(sayilar)
sayilarlist=list(sayilarset)
harflerlist=list(harfler)
print(f"{sayilarlist[1]}{harflerlist[1]}{harflerlist[0]}{harflerlist[3]}{harflerlist[6]}{sayilarlist[7]}{sayilarlist[25]}")
