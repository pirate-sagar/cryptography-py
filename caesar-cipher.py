alphabets="+=~`''""<>,.?/{}[]|\!@#$%^&*()_-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetsObj = {}
for i in range(0,len(alphabets)):
    alphabetsObj[alphabets[i]] = i

userText = input("enter text: ")

userText = userText.replace(" ","_")

userTextObj=[]

for i in range(0, len(userText)):
        userTextObj.append([userText[i],alphabetsObj[userText[i]]])

key=2

for i in range(0, len(userTextObj)):
        userTextObj[i][1]+=key

encryptedText=""

for i in userTextObj:
    key = next((k for k, v in alphabetsObj.items() if v == i[1]), None)
    encryptedText+=key

print("encrypted text",encryptedText)