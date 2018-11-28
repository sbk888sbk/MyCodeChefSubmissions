test_cases=int(input())
for test in range(test_cases):
    p1,p2,k=map(int, input().split())
    sum=p1+p2
    temp=sum%k
    if(sum<k*2):
        if sum < k:
            print("CHEF")
        else:
            print("COOK")
    else:
        if((sum-temp)%(k*2)==0):
            print("CHEF")
        else:
            print("COOK")

