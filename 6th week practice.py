# Set p,q
# n = p*q
# phi(n) = (p-1)*(q-1)
# 최소공약수 find e: gcd(phi(n),e)=1, 1<e<phi(n)
# find d: r*d mod phi(n)=1 , 1<d<phi(n)
# encrypt
# decrypt


# import math
from math import gcd


def setting(p: int, q: int):
    n = p * q
    phi_n = (p-1) * (q-1)
    e = find_e(phi_n)
    #print(e)
    d = find_d(phi_n, e)
    #print(d)
    
    return n, e, d
        
    
def find_e(phi_n: int):
    # import 사용시 _ math.gcd()
    e = 0
    for i in range(2, phi_n):
        if gcd(phi_n, i) == 1:
            e = i
            break
    return e


def find_d(phi_n: int, e: int):
    d = 0 
    for i in range(2, phi_n):
        if (e * i) % phi_n == 1:
            d = i
            break
            
    return d
            
    
def encrypt(plain_text: str, pub_key: list):
    # c = p^e mod n
    plain_bytes = [ord(x) for x in plain_text]
    #print(plain_bytes)
    cipher_bytes = []
    
    for i in plain_bytes:
        cipher_bytes.append((i ** pub_key[1] ) % pub_key[0])
    return cipher_bytes

def decrypt(cipher_list: list, pri_key: list):
  
    
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i ** pri_key[1]) % pri_key[0])
        
    
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text
    


if __name__=="__main__":
    p=11
    q=13
    n, e, d = setting(p, q)
    
    pub_key = [n, e]
    pri_key = [n, d]
    
    
    plain = "hello world"
    
    cipher = encrypt(plain, pub_key)
    #print(cipher)

    hex_list = []
    for i in cipher:
        hex_list.append(hex(i).split("x")[-1])
        #hex_list.append(hex(i).split("x")[1:])
        
    #print(hex_list)
    #print("".join(hex_list))
    #print("0x" + "".join(hex_list))
    
    hex_text = "0x" + "".join(hex_list)
    
    
    dec_plain = decrypt(cipher, pri_key)
    print(dec_plain)
    
   
    
    
