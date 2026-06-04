def print_list(list, idx=0):
    if( idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

names = ['Ankan', 'Arnab', 'jitu', 'goru']
print_list(names)