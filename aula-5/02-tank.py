# Buff de tank: crie 02-tank.py. Tank tem hp_base = 60000 e usa um skill que aumenta HP em 30%. Calcule hp_buffed. Depois, recebe uma tankbuster que tira hp_buffed - 8000. Imprima hp_apos_dano e o hp_percent resultante.

# Função para que calcule a soma de um valor mais sua porcentagem e traga na tela esse valor ja somado

hp_base = 60000
buff = 0.30
# Calcula o HP com o buff de 30% (60000 * 1.30 = 78000)
hp_buffed = hp_base * 1.30
# Dano recebido da tankbuster: tira 8000 do HP buffado
hp_apos_dano = hp_buffed - 8000 
# Porcentagem em relação ao HP máximo atual (hp_buffed)
hp_percent = (hp_apos_dano / hp_buffed) * 100

print(int(hp_buffed))
print(int(hp_apos_dano))
print(f"{hp_percent:.2f}")

