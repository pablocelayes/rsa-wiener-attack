import base64
import math

def decrypt(private_key): 

	with open('2.2_ciphertext.hex') as g:
		cipher = g.read()
	g.close()

	with open('2.2_modulo.hex') as h:
		modulo = h.read()
	h.close()

	text = pow(int(cipher, 16), int(private_key), int(modulo, 16))

	# cipher = AES.new(key, AES.MODE_CBC, iv)
	# decrypted =  cipher.decrypt(text)

	return str(text)