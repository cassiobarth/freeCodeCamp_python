even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
print()

teste = [var for var in 'variavel']
print(teste)
print()


numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
print()


resultado = [(('Par: ' + str(num)) if num % 2 == 0 else ('Ímpar: ' + str(num))) for num in numbers]
print(resultado)
print()

lista = [1, 2, 3, 4, 5]
resultado = [num * 2 for num in lista]
print(resultado)
print()

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long_word(word):
    return len(word) > 3

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']
print()

tipos_de_dados = [type(var) for var in [1, 2.0, 'three', True, None]]
print(tipos_de_dados) # [<class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>, <class 'NoneType'>]
print()

televisoes = ['Samsung', 'LG', 'Sony', 'Panasonic', 'Philips']
def is_not_samsung(tv):
    return tv != 'Samsung'

televisoes_nao_samsung = list(filter(is_not_samsung, televisoes))
print(televisoes_nao_samsung) # ['LG', 'Sony', 'Panasonic', 'Philips']


developer = 'Jessica'
print(list(developer))
