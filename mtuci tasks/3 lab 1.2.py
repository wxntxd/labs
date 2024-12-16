import  encodings
message = input("Enter your message:")
with open('message.txt' , 'w') as file:
    file.write(message)
print("Your message has been saved")
with open('message.txt' , 'a') as file:
    file.write(message)
print("Your message has been added ")
