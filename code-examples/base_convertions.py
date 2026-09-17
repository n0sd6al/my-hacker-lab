numbers = [0, 1, 2, 5, 7, 8, 10, 16, 31, 42, 64, 100, 127, 128, 200, 255, 256, 10000]

print(f'{"DEC":>6} | {"BIN":>10} | {"OCT":>6} | {"HEX":>6}')
print('-' * 38)

for n in numbers:
	b = format(n, 'b') # 'b' = binário, sem prefixo 0b
	o = format(n, 'o') # 'o' = octal
	h = format(n, 'X') # 'X' =  hexadecimal em maiúscula
	print(f'{n:>6} | {b:>10} | {o:>6} | 0x{h:<4}') # <4 alinha à esquerda

  

