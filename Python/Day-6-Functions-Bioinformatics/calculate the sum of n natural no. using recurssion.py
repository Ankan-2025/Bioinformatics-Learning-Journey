def cal_sum(n):
    if( n == 0):
        return 0
    return cal_sum(n-1) + n
A= int(input("Enter the value:"))
sum = cal_sum(A)
print(sum)
    