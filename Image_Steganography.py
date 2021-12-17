# pip install pycryptodome
# import DES3 for encryption and md5 for key

from Crypto.Cipher import DES3
from hashlib import md5

# for selecting encryption or decryption from given choice

while True:
 
 print('What do you want to do ?:\n\t1- Encrypt my Image\n\t2- Decrypt my Image')
 choice = input('Enter your choice here: ')
 
 if choice not in ['1', '2']:
  break
 
 # image/file path
 source = input('File path: ')

 # key for the triple DES algorithm
 key = input('TDES key: ')
 khash = md5(key.encode('ascii')).digest()
 key1_tdes = DES3.adjust_key_parity(khash)
 
 cipher = DES3.new(key1_tdes, DES3.MODE_EAX, nonce=b'0')
 
 # Open & read file from given path
 with open(source, 'rb') as i_file:
  file_to_be_encrypted = i_file.read()
  if choice == '1':
    # if choice is 1 encrypt
    new_file = cipher.encrypt(file_to_be_encrypted)
 
  else:
    # else decrypt
    new_file = cipher.decrypt(file_to_be_encrypted)
 
 # update values in the orginal file and save it
 with open(source, 'wb') as output:
  output.write(new_file)
  print('Execution Complete!')
  break