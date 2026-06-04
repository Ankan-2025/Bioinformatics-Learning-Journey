def print_list(items):
    print(len(items))

def print_elements(items):
    for item in items:
        print(item, end =' ')

names = ["Ankan", "Arnab", "Anurag"]
surnames =["chanda", "Dey", "Maity"]

print_list(names)
print_list(surnames)

print_elements(names)
print()
print_elements(surnames)

print()

def find_factorial(n):
    i=1
    count=1
    while(i <= n):
        count *= i
        i += 1
    print(count)
find_factorial(5)

def USD_converter(INR):
    print(95.81 * INR)

USD_converter(10)
