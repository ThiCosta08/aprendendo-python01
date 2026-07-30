hp_max = 9000
buff = 1.5
hp_buffed = hp_max * buff      # 13500.0

dano_recebido = 1234
hp_atual = hp_max - dano_recebido  # 7766

party_size = 8
gil_total = 80000
gil_por_pessoa = gil_total // party_size  # 10000 (divisão inteira)

hp = 5000
hp_max = 9000

print(hp == hp_max)   # False
print(hp < hp_max)    # True
print(hp != 0)        # True

job = "Paladin"
print(job == "Paladin")  # True
print(job != "Tank")     # True ("Paladin" não é literal "Tank")

print("Alphinaud" < "Alisaie")   # False (porque "p" > "l")
print("a" < "b")                  # True


em_combate = True
hp_baixo = True

precisa_curar = em_combate and hp_baixo   # True
fora_de_combate = not em_combate          # False

esta_em_dungeon = False
esta_em_raid = True
esta_em_grupo = esta_em_dungeon or esta_em_raid   # True

True  and True   # True
True  and False  # False
False and True   # False
False and False  # False

True  or True    # True
True  or False   # True
False or True    # True
False or False   # False

not True         # False
not False        # True

# Sem parênteses, ordem padrão funciona, mas é menos legível:
total = 100 + 50 * 2  # 200 (multiplicação primeiro)

# Com parênteses, intenção explícita:
total = 100 + (50 * 2)  # 200, idêntico, mas mais óbvio

# Forçar a soma primeiro:
total = (100 + 50) * 2  # 300

# Atribuição composta
# Os operadores +=, -=, *=, /=, //=, %=, **= são atalhos para “atualiza esta variável aplicando esta operação”.

hp = 9000
hp -= 1500     # hp = hp - 1500 → 7500
print(hp)

gil = 0
gil += 5000    # gil = gil + 5000 → 5000
gil += 12000   # 17000
print(gil)

contador = 1
contador *= 2  # 2
contador *= 2  # 4
contador *= 2  # 8

# Python aceita uma sintaxe que outras linguagens não aceitam: comparações encadeadas.

nivel = 47

if 30 <= nivel <= 50:
    print("Está na faixa de Heavensward")

    # Lê literalmente: “se 30 é menor ou igual a nivel, e nivel é menor ou igual a 50”. Mais limpo que if nivel >= 30 and nivel <= 50.





