def squaresum(n):
    sqrsum = 0
    
    for x in range(1, n+1):
        sqrsum = sqrsum + (x*x)
    return sqrsum

n = int(input('Enter number of natural numbers: ' ))    

print ('The sum of squares is ', squaresum(n))