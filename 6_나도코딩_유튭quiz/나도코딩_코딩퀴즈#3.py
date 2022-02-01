
for i in range(1,21):
#     # print("A{0} ".format(i),end='')
    if i % 2 == 1:
        print("A{0}".format(i), end=' ')
    
for i in range(1,21)[::2]: #슬라이싱 해서 한거(tip)
    print("A" + str(i), end = " ")