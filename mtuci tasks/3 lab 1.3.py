try:
    with open("example.txt" ,  "r" , encoding = 'utf-8') as file:
        content = file.read()
    print(content) # Чтение всего файла
    with (open("example.txt",  'r' ,  encoding = 'utf-8' ) as file):
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(" Файл  не существует.")