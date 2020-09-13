"""Você deve constiuir uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) motor
2) direção

O motor terá a responsabilidade de controlar a
 velocidade:
    Ele oferece os seuintes atributos:
    1) Atributo de dado velocidade
    2) Método acelerar, que deverá incrementar a velocidade de uma unidade
    3) Método frear que deverá decrementar a velocidade em duas unidades

    A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos
    1) valor de direção com valores possíveis: norte, sul leste, oeste
    2) Método girar_a_direita
    3) Método Girar_a_esquerda

    N
  O   L
    S
Exemplo:
# Testando motor
>>> motor = motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>> motor.acelerar()
>>> motor.velocidade
2
>> motor.acelerar()
>>> motor.velocidade
3
>>>motor.frear()
>>> motor.velocidade
1
>>>motor.frear()
>>> motor.velocidade
0

>>> # Testando Direção
>>> direção = Direção()
>>> direção.valor
'Norte'
>>> direção.girar_a_direita()
>>>direção.valor
'Leste'
>> direção.girar_a_direita()
>>>direção.valor
'Sul'
>> direção.girar_a_direita()
>>>direção.valor
'Oeste'
>> direção.girar_a_direita()
>>>direção.valor
'Norte'
>> direção.girar_a_desquerda)
>>>direção.valor
'Oeste'
>> direção.girar_a_desquerda)
>>>direção.valor
'Sul'
>> direção.girar_a_desquerda)
>>>direção.valor
'Leste'
>> direção.girar_a_desquerda)
>>>direção.valor
'Norte'
>>> Carro = Carro(direção, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direção()
>>> 'Norte'
>> carro.girar_a_direita()
>>>Carro.calcular_direcao
>>> 'Leste'
>> carro.girar_a_desquerda()
>>>Carro.calcular_direcao
>>> 'Norte'
>> carro.girar_a_desquerda()
>>>Carro.calcular_direcao
>>> 'Oeste'
"""