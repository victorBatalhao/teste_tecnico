while True:
    
    def fibonacci(n):
        sequencia = [0, 1]
        while sequencia[-1] + sequencia[-2] <= n:
            sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia

    def pertence_sequencia(n):
        sequencia = fibonacci(n)
        if n in sequencia:
            return f"O número {n} pertence à sequência de Fibonacci."
        else:
            return f"O número {n} não pertence à sequência de Fibonacci."

    n = int(input("Informe um número: "))
    print(pertence_sequencia(n))