* __MD5__: message digest system, aka Hash Function
	* This algorithm is not reversible, it's normally impossible to find the original word from the MD5.

* __Base64__: binary to text encoding
	* Capital letter, lower letter, number, + , /

* __DES__: symmetric-key algorithm
	* 56 bits key

* __AED__: symmetric-key algorithm
	* 128/192/256 bits key

* __RSA__: asymmetric public-private key cryptosystem
	* user encrypt message with pubic key, and owner decrypt it with private key. But for RSA, encryption can also be done with private key, and descryption with public key(not common).

* **Appendix**:

	* __Symmetric key vs asymmetric key__:
		* symmetric key is used to share info within a group
		* asymmetric key is mostly used for one way encryption and decryption

	* __SSL handshake__: both symmetic and asymmetric keys
		* 1. Client sends http request
		* 2. Server sends back a digital certificate with its asymmetric public key
		* 3. Client generates symmetric session key, encrypts it using the public key and sends it to the server
		* 4. Server decrypts session key using its asymmetric private key to get the symmertric session key
		* 5. Server and Client now encrypt and decrypt all data with symmetric session key
		* Reference: https://www.101computing.net/symmetric-vs-asymmetric-encryption/
