""" Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número 
informado pertence ou não a sequência. """

def sequenciaFibonacci(n):
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    return sequencia

def confirmaFibonacci(n):
    sequencia = sequenciaFibonacci(n+1)
    if n in sequencia:
        return True
    else:
        return False

n = int(input("Digite um número inteiro: "))
if confirmaFibonacci(n):
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
