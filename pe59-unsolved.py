# read in message
f = open('pe59.txt', 'r')
message = [int(x) for x in f.read().split(',')]
f.close()

# msg and key are lists of ascii values
def decrypt(msg, key):
	decoded = msg[:]
	key_len = len(key)
	for i in range(0, len(decoded)):
		decoded[i] = decoded[i] ^ key[i%key_len]
	return decoded

def msg_to_ascii(msg):
	return ''.join([str(unichr(x)) for x in msg])

def str_to_key(strng):
	return [ord(c) for c in strng]

def all_chars(strng):
	result = True
	for c in strng:
		result = result and ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('a') and ord(c) <= ord('z')))
	return result

print ord('a')
messages = []
for i in range(97, ord('z')+1):
	for j in range(97, ord('z')+1):
		for k in range(97, ord('z')+1):
			messages.append(msg_to_ascii(decrypt(message, [i,j,k])))

messages = filter(lambda x: all_chars(x), messages)
