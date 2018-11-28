hosted_year=list((2010, 2015, 2016, 2017 , 2019))
test_cases=int(input())
for test in range(test_cases):
    N=int(input())
    if(N in hosted_year):
        print("HOSTED")
    else:
        print("NOT HOSTED")
