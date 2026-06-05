with open("practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning File I/O \nusing Java. \nI am programming in Java.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

word = 'learning'
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")

def check_for_line():
    word = "python"
    data = True
    line_number = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_number)
                return
            line_number += 1

    return -1
print(check_for_line())