heroi = {
    'nome': "Inosuke",
    'exp': 10001,
}

if heroi['exp'] <= 1000:
    print(f"O herói {heroi['nome']} está no nível Ferro")
elif not heroi['exp'] < 1001 and heroi['exp'] <= 2000:
    print(f"O herói {heroi['nome']} está no nível Bronze")
elif not heroi['exp'] < 2001 and heroi['exp'] <= 5000:
    print(f"O herói {heroi['nome']} está no nível Prata")
elif not heroi['exp'] < 6001 and heroi['exp'] <= 7000:
    print(f"O herói {heroi['nome']} está no nível Ouro")
elif not heroi['exp'] < 7001 and heroi['exp'] <= 8000:
    print(f"O herói {heroi['nome']} está no nível Platina")
elif not heroi['exp'] < 8001 and heroi['exp'] <= 9000:
    print(f"O herói {heroi['nome']} está no nível Ascendente")
elif not heroi['exp'] < 9001 and heroi['exp'] <= 10000:
    print(f"O herói {heroi['nome']} está no nível Imortal")
elif heroi['exp'] >= 10001:
    print(f"O herói {heroi['nome']} está no nível Radiante")
