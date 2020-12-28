import re
from itertools import cycle

#подготовка текста
def cleaner(file):
    with open(file) as dirty:
        text = dirty.read().lower().replace('ё', 'е')
        text = re.sub('[^а-я]','', text)
        return text

#интерпретатор
def chr_to_int(char):
    return 0 if char == 'а' else ord(char)-1072

#обратный интерпретатор
def int_to_chr(integer):
    return 'а' if integer == 0 else chr(integer+1072)

#шифрование
def add_chars(a, b):
    return int_to_chr(( chr_to_int(a) + chr_to_int(b)) % 32 )

#шифровшик текста
def encrypter(text, key):
    keystream = cycle(key)
    encrypted = ''
    for msg, key in zip(text, keystream):
        if msg == ' ':
            encrypted += ' '
        else:
            encrypted += add_chars(msg, key)
    return encrypted

#индексатор
def indexer(text):
    len_of_text = len(text)
    letters_map = {i:0 for i in letters}
    for letter in text:
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            continue
    arr = sum([letters_map[item] * (letters_map[item] - 1) for item in letters_map])
    div = len_of_text * (len_of_text - 1)
    result = arr / div
    return result

#дешифрование
def add_chars2(a, b):
    return int_to_chr(( chr_to_int(a) - chr_to_int(b)) % 32 )

#дешифровщик
def decrypter(text, key):
    keystream2 = cycle(key)
    decrypted = ''
    for msg, key in zip(text, keystream2):
        if msg == ' ':
            decrypted += ' '
        else:
            decrypted += add_chars2(msg, key)
    return decrypted

#частоты
word_fr = {'а': '0.08267',
 'б': '0.01787',
 'в': '0.04306',
 'г': '0.01597',
 'д': '0.03169',
 'е': '0.08788',
 'ж': '0.01063',
 'з': '0.01618',
 'и': '0.06673',
 'й': '0.01210',
 'к': '0.03309',
 'л': '0.04911',
 'м': '0.03424',
 'н': '0.06605',
 'о': '0.10897',
 'п': '0.02385',
 'р': '0.04139',
 'с': '0.05668',
 'т': '0.06016',
 'у': '0.02625',
 'ф': '0.00142',
 'х': '0.00788',
 'ц': '0.00292',
 'ч': '0.01534',
 'ш': '0.00846',
 'щ': '0.00315',
 'ъ': '0.00021',
 'ы': '0.01991',
 'ь': '0.02139',
 'э': '0.00498',
 'ю': '0.00547',
 'я': '0.02434'}


letters = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
alph_len = len(letters)
letters_map = {letters[key] : key for key in range(alph_len)}
numbers_map = {key : letters[key] for key in range(alph_len)}
arr_of_keys = ['ад','рай','киев','одесса', 'величественный']
text = cleaner("vusotsky.txt")
print()
print("инднекс совпадений для открытого текста: {}".format(indexer(text)))
print()


for k in arr_of_keys:
    print('Для ключа:', '(', len(k), ')', k)
    key = k
    encrypted = encrypter(text, key)
    print('Ваш зашифрованый текст: ', encrypted)
    arr_index = {}
    print("Инднекс совпадений для шифр текста ключом длинной {}: {}".format(len(k),indexer(encrypted)))
    print()
    arr_index[len(k)] = indexer(encrypted)

#функция произвольного ключа
def asker(text):
    print('Введите свой ключ шифрования: ')
    key = input()
    print()
    print('Для ключа:', '(',len(key),')', key)
    encr = encrypter(text, key, )
    print(encr)
    print()
    print()


ask = asker(text)


unkey = encrypter('юогвмахейибдвийнь','да')
ecnry_text = cleaner('var6.txt')
decrypted = decrypter(ecnry_text, unkey )
print('Шифрованый текст варианта 6')
print(ecnry_text)
print()
print('Ключ зашифрованого текста var6.txt :{}'.format(unkey))
print()
print('Расшифрованый текст:')
print(decrypted)
open('decrypted','w').write(decrypted)