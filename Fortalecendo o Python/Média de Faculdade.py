n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 8:
    print(f"Aprovado com média {media:.2f}")
else:
    print(f'Não foi aprovado, sua nota foi {media:.2f} e será necessário fazer a prova final.')
    n3 = float(input("Digite a terceira nota: "))

    media_final = (media + n3) / 2

    if media_final >= 5:
        print(f"Aprovado na prova final com média {media_final:.2f}")
    else:
        print(f"Reprovado na prova final com média {media_final:.2f}")