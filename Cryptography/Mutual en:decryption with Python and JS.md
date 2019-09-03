# Mutual en/decryption with Python and JS

## Background


There appears to be a full spectrum of text encoding and decoding methods. Here is a quick rundown of those options and why AES is the best solution for encryption/decryption.

* __MD5__: message digest. This algorithm is not reversible, i.e. no decryption.
* __Base64__: binary to text encoding and decoding. Simple encryption and decryption. Not very secure.
* __DES__: symmetric-key algorithm. Relatively short key. Known for security vulnerability. 
* __RSA__: asymmetric public-private key crypto system. Design for multiple parties one-way encryption/decryption. Not suit to internal system encryption/decryption.

Then, one crypto method stands out that appears to meet the requirements:
* __AES__: symmetric-key algorithm. 
  * Key size from 128/192/256 bits
  * Python and JavaScript implementation
  * Encryption and decryption within a group

Here are typical AES settings:
* __Key__: 256 bits Hexdecimal
* __IV__: 128 bits Hexdecimal
* __Mode__: CBC (CryptoJS default)
* __CMS__: PKCS7 (CryptoJS default)

Note: 

* Key and iv are created with OpenSSL, and stored as environment variables:
* CLI command to generate key and iv: ```openssl enc -aes-256-cbc -k secret -P -md sha1```
* Both key and iv should be in HEX format.

# Python
* Requirements
  * [Pycrypto](https://pypi.org/project/pycrypto/)

* Implementation

```
import base64  
from Crypto.Cipher import AES

def encrypt(key, iv, plain_text):  
padded_text = CryptoHelper._pad(plain_text)  
cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))  
encrypted_text = base64.b64encode(cipher.encrypt(padded_text))  
return encrypted_text  

def decrypt(key, iv, encrypted_text):  
encrypted_text_b64decoded = base64.b64decode(encrypted_text)  
cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))  
unpadded_text = CryptoHelper._unpad(cipher.decrypt(encrypted_text_b64decoded))  
plain_text = unpadded_text.decode(encoding="utf-8")  
return plain_text  

def _pad(string):  
block_size = AES.block_size  
string = string.encode("utf-8")  
return string + (block_size - len(string) % block_size) * chr(block_size - len(string) % block_size).encode("utf-8")  

def _unpad(string):  
return string[:-ord(string[len(string) - 1:])]
```

# JavaScript
* Requirement:
  * [crypto-js](https://www.npmjs.com/package/crypto-js)
  
* Implementation:

```
CryptoJS = require("crypto-js");

function encrypt(key, iv, plain_text) {

var key_binary = CryptoJS.enc.Hex.parse(key)
var iv_binary = CryptoJS.enc.Hex.parse(iv)
var encrypted_text = CryptoJS.AES.encrypt(plain_text, key_binary, { iv: iv_binary });
return encrypted_text;
}

function decrypt(key, iv, encrypted_text) {
var key_binary = CryptoJS.enc.Hex.parse(key)
var iv_binary = CryptoJS.enc.Hex.parse(iv)
var plain_text = CryptoJS.AES.decrypt(plain_text, key_binary, { iv: iv_binary });
return plain_text;
}

```

# Example

1. Encryption in nodeJs
``` var encrypted_text = encrypt(key, iv, "Hello World")```

2. Decryption in Python
``` plain_text = decrypt(key, iv, "3QwLF8qtxYoRdHxr/2i13A==")``` 
