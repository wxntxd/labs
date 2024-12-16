import encodings
with open("example.txt" ,  "r" ) as file:
    content = file.read()
print(content) # Чтение всего файла
with open("example.txt",  'r' , ) as file:
        for line in file:
            print(line.strip())

