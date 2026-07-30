# GCD timer: crie 03-gcd.py. Em FFXIV o GCD base é 2.5 segundos. 
# Calcule quantas habilidades dá pra usar em uma janela de 60 segundos
# (use //). 
# Imprima a resposta no formato Em 60 segundos cabem N habilidades GCD.

gcd = 2.5
janela = 60
# Divisão inteira (//) para encontrar a quantidade de habilidades
habilidades = int(janela // gcd)

# Saída formatada
print(f"Em {janela} segundos cabem {habilidades} habilidades GCD.")