print('Crypto - Encoder')

def encodedecode():
	real = 'abcdefghijklmnopqrstuvwxyz!'
	code = real[-1] + real[0:-1]
	
	real_dict = dict(zip(real, code))
	code_dict = dict(zip(code, real))

	message = input('Enter the secret message: ').lower()
	mode = input('Specify the mode: encode (e) / decode (d): ').lower()

	if mode == 'e':
		message1 = ''.join([real_dict[n] for n in message])
	elif mode == 'd':
		message1 = ''.join([code_dict[n] for n in message])
	else:
		print('Error! Invalid Mode!')

	print(message1)


encodedecode()