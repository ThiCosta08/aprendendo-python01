possui_tomestones = int(input("Quantas tomestones tem: "))
preco_peca_gear = 500

pecas = possui_tomestones // preco_peca_gear
sobra = possui_tomestones % preco_peca_gear

print()
print(f"Com: {possui_tomestones}, você pode comprar: {pecas} peça(s) e sobram {sobra}.")

