from random import randint

with open('output.txt','w') as fw:
    for i in range (10): fw.write(str(randint(1,1000))+',')

with open('output.txt','r') as fr:
    a=fr.readline().split(',')
    a.pop()
    print (sorted(map(int, a)))