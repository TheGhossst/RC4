# RC4
Just a basic RC4 algorithm done in python  
Steps:  
# 1.Array Initialization    
Initialize a character array 'S' of size 256 or the key size  
```bash
for i in range(256): S[i] = i
 ```   
# 2.Key Scheduling Algorithm (KSA)  
A temp vector T is created    
If key len is 256 then T=K    
```bash
T[i]=K[i]
```
Else the first k-len elements of T are copied from K    
```bash 
T[i]=K[i mod(k-len)]
```    
```bash
for i in range(256):
    j=(j+S[i]+T[i]) % 4
    swap(S,i,j)
```            
# 3. Pseudo Random Generator Algorithm (PGRA)
```bash
while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        swap(S, i, j)
        key_byte = S[(S[i] + S[j]) % 256]
        result.append(key_byte ^ byte)
```
# 4. Encryption Process
XOR key_byte and the plain text

# The question based on which rc4test.py is implemented on

Assume a 4 x 3 bit key 'k' and plain text 'p' as given  
``
k=[1 2 3 6]
``  
``
p=[1 2 2 2]
``  
Perform encryption using RC4 algorithm
