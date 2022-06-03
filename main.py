# inputs need to give
requirements = ['gym','store','school','barber']
blocks = [
        {'gym':True,'store':True,'school':True,'barber':False},
        {'gym':True,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':False,'barber':False},
        {'gym':False,'store':False,'school':True,'barber':False},
        {'gym':True,'store':True,'school':False,'barber':False}, #this is correct, because distanse to go everyday is 2
        {'gym':False,'store':False,'school':False,'barber':True}
]

#varibales for code

dis = []
result = 99999999
count = 0
best_block = ''

for i in blocks:
    for y in range(len(requirements)):
        try:
            dis[y]
        except:
            dis.append(99999999)

        if i[requirements[y]] == False:
            if dis[y] != 99999999:
                dis[y] = dis[y] +1
            i[requirements[y]+"_dis"] = dis[y]
        else:
            i[requirements[y]+"_dis"] = 0
            dis[y] = 0

dis = []

for i in reversed(blocks):
    for y in range(len(requirements)):

        try:
            dis[y]
        except:
            dis.append(99999999)

        if i[requirements[y]] == True:
            dis[y] = 0
        else:
            dis[y] += 1
            i[requirements[y]+"_dis"] = min(dis[y],i[requirements[y]+"_dis"] )
            
for i in blocks:
    for y in range(len(requirements)):
        count += i[requirements[y]+"_dis"]

    result = min(count,result)
    if count <= result:
        best_block = i

    count = 0

print(f"between these blocks : {blocks}. \n This block is best : {best_block}. \n And the distanse between requirements is {result} .")


#Tasks : 100%
#time : N 2N**K
#All : 85%

