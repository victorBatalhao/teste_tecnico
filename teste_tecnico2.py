def verifica_a(string):
    a_maiuscula = string.upper().count('A')
    a_minuscula = string.lower().count('a')
    a_total = a_maiuscula + a_minuscula
    if a_total > 0:
        return f"A letra 'a' ocorre {a_total} vezes na string."
    else:
        return "A letra 'a' não ocorre na string."

# Exemplo de uso:
#string = input("Informe uma string: ")
string = "Esta é uma string com a letra 'a' maiúscula e minúscula."

print(verifica_a(string))