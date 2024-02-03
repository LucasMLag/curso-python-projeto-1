# Aula 4: tipos int, float

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.

# Exemplos de int:

print(1)
print(0)
print(-1)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.

# Exemplos de float:

print(1.1, 1.2, 1.3)
print(-1.1, -1.2, -1.3)
print(0.0, 1.0, 2.0)

# A função type mostra o tipo que o Python
# inferiu ao valor.

print(type('Texto'))  # Type = <class 'str'>
print(type(1))  # Type = <class 'int'>
print(type(1.0))  # Type = <class 'float'>