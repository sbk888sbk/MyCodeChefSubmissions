test_cases=int(input())
for test in range(test_cases):
    N=int(input())
    S=input()
    if(N%2==0):
        length=N-1
    else:
        length=N-2

    string_list=list(S)

    for i in range(0,length,2):
        string_list[i],string_list[i+1]=string_list[i+1],string_list[i]

    for k in range(N):
        string_list[k]=(chr((122-ord(string_list[k]))+97))
    S=''.join(string_list)
    print(S)
