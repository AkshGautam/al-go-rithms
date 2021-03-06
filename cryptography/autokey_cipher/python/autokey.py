# It uses the following Table called Tabula Recta to find the
# ciphertext. The simple intersection of the row and column
# is the ciphertext. Let's say for eg. T is the Key and E is
# the original Plaintext, then the intersection of T column
# and E row is the ciphertext i.e. X. The plaintext and key-
# length must be the same. Autokey Cipher is similar to 
# Vigenere Cipher. The only difference lies in how the key is 
# chosen. In Vigenere, any random key is chosen which is 
# repeated till the length of the plaintext. In Autokey, 
# the key chosen contains some part of the plaintext itself.

#     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#     ---------------------------------------------------
# A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

plaintext = 'DEFENDTHEEASTWALLOFTHECASTLE'
key = 'FORTIFICATIONDEFENDTHEEASTWA'
ciphertext = ''

if __name__ == '__main__':	
	for index in xrange(len(plaintext)):
		sum_key_plaintext = (ord(key[index]) - 64) + (ord(plaintext[index]) - 64)
		if sum_key_plaintext > 27:
			ciphertext += chr(sum_key_plaintext - 26 - 1 + 64)
		else:
			ciphertext += chr(sum_key_plaintext - 1 + 64)	
	print ciphertext
