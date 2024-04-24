#!/usr/bin/python3

def pascal_triangle(n):
    if n > 0:
        l = [0, 1, 0]
        m = [[1]]
        #print([1])
        for x in range(n - 1):
            k = []
            for t in range(len(l)):
                if t == 0:
                    #print(t)
                    k.append(l[0])
                else:
                    #print(t)
                    k.append(l[t] + l[t-1])

            k.append(l[t])
            #m.append(k)
            m.append(k[1:-1])
            l = k
        return m
    else:
        return []
