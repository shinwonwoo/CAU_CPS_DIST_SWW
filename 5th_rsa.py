
p = 17
q = 19
n = p * q
phi_n = (p-1) * (q-1)

e = 17

d = 0
mod = 0
while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break

# Encryption
# C = P^e mod n

plain = "CAU CPS DIST"
plain_list = [ord(x) for x in plain]

#for x in plain:
 #   ord(x)
  #  plain_list.append(ord(x))

##print(plain_list)

cipher = []
for i in plain_list:
    x = (i**e) % n
    cipher.append(int(x))

# print(cipher)

# Decryption
# P = C^d mod n

decryted = []
for i in cipher:
    x = (i**d) % n
    decryted.append(int(x))

print('plain text', plain_list)
print('cipher text', cipher)
print('decryted text', decryted)

# 문자를 아스키 코드로 바꾸는 함수 chr()
# join 함수의 필요성
print([chr(x) for x in decryted])
decryted_text = ''.join([chr(x) for x in decryted])
print(decryted_text)






