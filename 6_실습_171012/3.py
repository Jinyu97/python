for i in range(9,0,-1):
    for j in range(1,8):
        if 4<i<9 and j>5:
            break
        print('%4d'%(i*100+j),end='')
    print()