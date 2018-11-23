def max(l):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            print("l[i]:{0},l[j]:{1}".format(l[i],l[j]))
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
    return l

if __name__ == "__main__":
    array = [2,3,1,6,7,5,8,9,10,4]
    array1 = max(array)
    print('从大到小依次为:{}'.format(array1))
                
