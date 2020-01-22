canonstr = input("Введите сообщение которое хотите зашифровать:\n").lower()
key = int(input("Введите код шифрования: "))
outstr = ''

for i in range(len(canonstr)):
    if canonstr[i] == ' ':
        outstr += ' '
    elif 'a' <= canonstr[i] <= 'z':
        outstr += chr((ord(canonstr[i])-key - 96)%26 + 96)
    else:
        outstr += chr((ord(canonstr[i])-key - 1071)%32 + 1071)
print (outstr)
