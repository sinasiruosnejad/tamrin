def string_to_list():
    x=input()
    result=[]
    i=1
    while x[i]!=']':
        if x[i]!=',':
            j=i
            temp=''
            while x[j]!=',':
                if x[j]==']':
                    break
                temp+=x[j]
                j+=1
                i=j
            result.append(int(temp))
        else:
            i+=1
    return result

def prime(x):
    prime_numbers=[]
    for i in range(2,x+1):
        for j in range(2,i):
            if (i % j) == 0:  
                break  
        else:
            prime_numbers.append(i) 
    return prime_numbers

def Decomposition(num):
    count=0
    primes=prime(num)
    while num>2:
        for i in range(len(primes)):
            if num%primes[i]==0:
                num/=primes[i]
                count+=1
    return count



lis=string_to_list()
result={}
for i in range(len(lis)):
    temp=Decomposition(lis[i])
    result.update({str(lis[i]):temp})

final=[0,0]
for i in result:
    if final[1]<result[i]:
        final[1]=result[i]
        final[0]=i

print(f"{final[0]} : {final[1]}")