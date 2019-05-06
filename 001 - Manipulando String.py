
# Este exercicio visa a manipulação de uma String Alfanumérica
# com objetivo de verificar varias diferentes manipulações em Fatiamento

palavra = 'paralelepipedo'

# inicio na casa 4 ate a casa 7
print('inicio na casa 4 ate a casa 7: ',palavra[3:7])

# primeiras 2 chars
print('primeiras 2 chars: ',palavra[0:2])

# ultimas 2 chars
print('ultimas 2 chars: ',palavra[:2])

# a partir da casa 3 devido ao índice iniciar no 0
print('a partir da casa 3: ',palavra[2:])

# exibir ate a penultimo chars
print('exibir ate a penultimo: ',palavra[0:-2])
