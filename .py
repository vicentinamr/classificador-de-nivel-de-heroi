# Declaração das variáveis
nome = "Lúcifer"
xp = 10000

# Estrutura de decisão
if xp < 1000:
    nivel = "Ferro"
elif xp >= 1001 and xp <= 2000:
    nivel = "Bronze"
elif xp >= 2001 and xp <= 5000:
    nivel = "Prata"
elif xp >= 5001 and xp <= 7000:
    nivel = "Ouro"
elif xp >= 7001 and xp <= 8000:
    nivel = "Platina"
elif xp >= 8001 and xp <= 9000:
    nivel = "Ascendente"
elif xp >= 9001 and xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Saída
print(f"O Herói de nome {nome} está no nível de {nivel}")
