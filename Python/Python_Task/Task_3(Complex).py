import cmath
z=3+4j
print(z.real)  
print(z.imag)

a=3+4j
b=1+2j
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(abs(z))
print(z.conjugate())

z=1+1j
print(cmath.sqrt(z))  
print(cmath.polar(z))
print(cmath.phase(z))
