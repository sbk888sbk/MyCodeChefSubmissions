test_cases=int(input())
for test in range(test_cases):
    a,b,c=map(int, input().split())
    # a = int(input())
    # b = int(input())
    # c = int(input())
    flag=0


    if( a + b - c ==0 ):
        flag=1
    elif( a - b + c == 0):
        flag = 1
    elif( c + b - a == 0):
        flag = 1

    if(flag==0):
        print("no")
    else:
        print("yes")
