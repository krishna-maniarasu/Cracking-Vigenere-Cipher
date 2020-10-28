from math import gcd
import numpy as np

def shift(A,n):
    return A[n:]+A[:n]

Freq = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher=input("Enter the ciphertext").lower()
length=len(cipher)
A=[]
ci=list(cipher)
c=ci
#######  Find the number of coincidences by shifting the ciphertext ###########
k=1
while k<=30:
    l=c[length-1]
    for val in range(length-1,0,-1):
        c[val]=c[val-1]
    c[0]=l
    count=0
    for i in range(k,length):
        if c[i]==cipher[i]:
            count+=1
    print("Number of coincidences for",k,"displacement is",count)
    A.append(count)
    k=k+1
print(A)

######### Finding first 6 maximum coincidences and its displacement ############
B=sorted(set(A))
KeyLengths=[]
for i in range(1,7):
    print(i," st Maximum number of coincidences is",B[-i])
    KeyLengths.append(A.index(B[-i])+1)
print("Possible Keys Lengths",KeyLengths)
########################  FINDING THE KEYWORD  ###############################
nn=0
while nn<=3:
    L=KeyLengths[nn]
    print("\nTaking",L,"as key length",end="\n")
    z=[[] for i in range(0,L)]
    v=0
    while v<L:
        for i2 in range(v,len(cipher),L):
            z[v].append(cipher[i2])
        v+=1
    v=0
    array=""
    while v<L:
        w=[]
        for char in letters:
            y=z[v].count(char)
            y=round(y/26,7)
            w.append(y)
        J=[]
        i=0
        while i<26:
            S=shift(Freq,i)
            K = np.dot(w,S)
            K = round(K,7)
            J.append(K)
            i+=1
        prod=max(J)
        g=J.index(prod)
        kk=(26-g)%26
        array+=(chr(kk+97))
        v+=1
    print("The Encryption key is \"",array,"\"",end="\n")
    ############ DECRYPT THE CIPHER TEXT USING KEYWORD #############
    print("Plain text is",end="\n")
    for i in range(0,length):
        p=cipher[i]
        k=array[i%L]
        ans= ((ord(p)-97)-(ord(k)-97))%26
        print(chr(ans+97),end="")
    nn+=1
    print("\n")
