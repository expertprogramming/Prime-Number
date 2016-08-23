start=int(input("Eneter start number"))
end=int(input("Enter end number"))
#num=start
while(start<=end):
    count=0
    i=2
    while(i<=start/2):
        if(start%i==0): #number is not prime
            count+=1
            break 
        i+=1
    if(count==0 and start!=1):
        print("prime number ",start)
    start+=1
