# RC4
Just a basic RC4 algorithm done in python  
Steps:  
**1.Array Initialization**  
Initialize a character array 'S' of size 256 or the key size  
```bashfor i in range(256): S[i] = i ``` 
**2.KSA**  
A temp vector T is created  
If key len is 256 then T=K  
Else the first k-len elements of T are copied from K  ``bash T[i]=K[i mod(k-len)]``  
```bashfor i in range(256):                
        j = (j + S[i] + key[i % key_length]) % 256                      
        swap(S, i, j) ```                 

