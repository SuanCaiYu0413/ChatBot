# coding:utf-8
import random
a = []
b = []

with open('xiaohuangji50w_nofenci.conv') as fp:
    line = fp.readline()
    q = True
    while line:
        if line.strip()[0:1] == 'M':
            if q == True:
                q = False
                a.append(line.strip()[1:len(line)])
            else:
                q = True
                b.append(line.strip()[1:len(line)])
        line = fp.readline()

    fp.close()

c = []
d = []

for i in range(3000):
    index = random.randint(0,len(a)-1)
    c.append(a[index])
    d.append(b[index])

with open('./samples/question','w') as fp:
    for line in c:
        fp.write(line + '\n')

    fp.close()



with open('./samples/answer','w') as fp:
    for line in d:
        fp.write(line + '\n')

    fp.close()