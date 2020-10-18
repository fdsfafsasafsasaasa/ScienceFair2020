# Can modern encryption be bruteforced?


http://mathaware.org/mam/06/Kaliski.pdf


Steps to generate RSA key:
Generate random primes: p and q
Generate n: p*q
Generate M and C: 
    M and C = random integer between 0 and n -1
    E is an odd integer between 3 and n -1 that is relativey prime to p-1 and q-1
    c = m^e modulo n
    d = odd integer between 3 and n-1
    m = (m^e)^d % n
