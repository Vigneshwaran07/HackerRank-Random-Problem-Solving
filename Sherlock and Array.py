def solve(a):
    # Complete this function
    summy=sum(a)
    l=len(a)
    lefty=0
    for i in range(len(a)):
        current=a[i]
        summy-=current
        if lefty==summy:
            return 'YES'
        lefty+=current
    return 'NO'
