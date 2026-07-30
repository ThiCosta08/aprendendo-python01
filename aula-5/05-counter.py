# Atribuição composta: crie 06-counter.py que começa com gil = 0,
# e simula sete ações: ganhou 5000, gastou 200, ganhou 1500, 
# gastou 80% (use *= 0.2 que sobra 20%, ou -= gil * 0.8),
# ganhou 10000, gastou 3333, gastou 1.
# Imprima gil ao fim.
# Confira no papel se bate.

gil = 0 
gil += 5000
gil -= 200
gil += 1500
gil -= gil * 0.8
gil += 10000
gil -= 3333 
gil -= 1 

print(gil)
