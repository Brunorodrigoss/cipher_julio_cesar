import json

from hash import apply_sha1
from util import create_json_file, update_json_file
from request import get_request, post_request

response = get_request()
data = json.dumps(response.json())

create_json_file(data)

json_response = response.json()
house_number = json_response['numero_casas']
cipher_text = str(json_response['cifrado'])

print(f'House number: {house_number}')
print(f'Cipher text: {cipher_text}\n')

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
deciphered_text = ''

for word in cipher_text.lower():
    if str(word).isspace() or word == '.':
        deciphered_text += word
    else:
        position = alphabet_list.index(word)
        letter = alphabet_list[(position - house_number)]
        deciphered_text += letter

print(f'Deciphered text: {deciphered_text}')

update_json_file("decifrado", deciphered_text)

sha1 = apply_sha1(deciphered_text)
update_json_file("resumo_criptografico", sha1)
print(f'sha1: {sha1}')

post_request()

