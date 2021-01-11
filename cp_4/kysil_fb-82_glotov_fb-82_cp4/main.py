import math, random, requests, json
from bs4 import BeautifulSoup

data = requests.get('https://miniwebtool.com/list-of-prime-numbers/?to=10000').content
soup = BeautifulSoup(data, 'html.parser')
tenk_primes = soup.find('div',class_='r2').text
tenk_primes = list(map(int,tenk_primes.split(',')))

def findModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def miller_rabin(num):
    for prime in tenk_primes:
        if num % prime == 0:
            return False
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True




def random_prime_from_interval(keysize,name):
    while True:
        n0 = 2**(keysize-1)
        n1 = 2**(keysize)
        num = random.randrange(n0, n1)
        if miller_rabin(num):
            return num
        else:
            print(f"число {num} не прошло на роль {name} потму что завалило тест миллера рабина")

def geretate_rsakeys(amount_of_bits):
    p = random_prime_from_interval(amount_of_bits//2,'p')
    q = random_prime_from_interval(amount_of_bits//2,'q')
    n = p*q
    fin = (p-1)*(q-1)
    e = 2**16+1
    d = findModInverse(e, fin)
    return (p,q,fin,n,e,d)

def cripter(M,e,n):
    C = pow(M, e, n)
    return C

def decrytper(C, d, n):
    M = pow(C, d, n)
    return M

def sign(M, d, n):
    S = pow(M, d, n)
    return (M, S)

def singchecker(M, S, e, n):
    return M == pow(S, e, n)

def sender(e,n,d,e1,n1):
    print("key sender")
    if n1 < n: return None
    k = random.randint(1, n-1)
    print('k =', hex(k))
    k1 = cripter(k,e1,n1)
    print('k2 =', hex(k1))
    _,S = sign(k,d, n)
    print('s =', hex(S))
    _,S1 = sign(S,e1,n1 )
    print('s1 =', hex(S1))
    return (k1,S1)

def reciver(k1_S1, e1, n1, d1, e, n):
    k1,S1 = k1_S1
    print('n =', hex(n))
    print('e =', hex(e))
    print('n1 =', hex(n1))
    print('e1 =', hex(e1))
    print('k1 =', hex(k1))
    print('s1 =', hex(S1))
    print('d1 =', hex(d1))
    _,S = sign(S1,n1)
    print('s1 =', hex(S))
    print(' =', hex(n))
    k = decrytper (k1, d1, n1)
    print('k =', hex(k))
    print("s^e modn={}", hex(pow(S, e, n)))
    return k == pow(S, e, n)

request1 = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=256')
cookie = request1.cookies
n1 = request1.text
n1 = json.loads(n1)['modulus']
n1 = int(n1,16)
e1 = 65537
p,q,fin,n,e,d = geretate_rsakeys(256)
while n > n1:
    p,q,fin,n, e, d = geretate_rsakeys(256)
print('n1 сайта', hex(n1))
print('e1 сайта', hex(e1))

print(f"""
    p користувача denys {hex(p)},
    q користувача denys {hex(q)},
    функція ойлера користувача {hex(fin)}
    e користувача denys {hex(e)},
    n користувача denys {hex(n)},
    d корисувача denys {hex(d)}
""")


k1,s1=sender(e,n,d,e1,n1)
request2 = f"http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={hex(k1)[2:]}&signature={hex(s1)[2:]}&modulus={hex(n)[2:]}&publicExponent={hex(e)[2:]}"
print("ответ ReciveKey сайта: ")
print(requests.get(request2,cookies=cookie).text)
