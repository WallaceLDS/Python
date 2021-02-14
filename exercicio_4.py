N = int(input(""))
for i in range(N):
    Line= input("")
    total = 0
    menor = 0
    for j in range(len(Line)):
        if(Line[j] == "<"):
            menor += 1
        if(Line[j] == ">" and menor > 0):
            total += 1
            menor -= 1
    print(total)            
