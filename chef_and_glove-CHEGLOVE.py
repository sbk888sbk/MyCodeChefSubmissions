def check_true(fingers_num, sheath_len):
    for i in range(fingers_num):
        if fing_len[i] <= sheath_len[i]:
            pass
        else:
            return False
    return True

test_cases=int(input())
for test in range(test_cases):
    fingers_num=int(input())
    fing_len=list(map(int, input().split()))
    sheath_len=list(map(int, input().split()))
    front=check_true(fingers_num,sheath_len)
    sheath_len.reverse()
    back=check_true(fingers_num,sheath_len)
    if(front and back):
        print("both")
    elif(front):
        print("front")
    elif(back):
        print("back")
    else:
        print("none")
