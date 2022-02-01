# b07502139 機械四 盧演整

# fin = open("/Users/noyeonjeong/Desktop/python workspace/Data/yob1880.txt", 'r')
# fin_read = fin.readlines()

for year in range(1880, 2021):
    boys = 0
    girls = 0
    fin = open(f"/Users/noyeonjeong/Desktop/python workspace/Data/yob{year}.txt", 'r')
    fin_read = fin.readlines()

    for i in range(len(fin_read)):
        index_1 = fin_read[i].index(",")
        index_2 = fin_read[i].index(",", index_1 + 1)
        number = int(fin_read[i][index_2+1 : -1])
        # man = person.index("M", index_1 + 1) #숫자
        # female = person.index("F", index_1 + 1)
    
        if fin_read[i][index_2-1 : index_2] == "M": # 만약 남자라면
            boys += number
        if fin_read[i][index_2-1 : index_2] == "F":
            girls += number
    if boys > girls:
        print(f'Year {year} : more boys - {boys} > {girls}')
    else: 
        print(f'Year {year} : more girls - {girls} > {boys}')
    
print(110490 + 90994)
print(1706423 + 1598836)




