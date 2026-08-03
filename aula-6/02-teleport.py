gil_atual = int(input("Gil Atual: "))
teleport_custo = int(input("Custo do teleporte: "))

gil_restante = gil_atual - teleport_custo

print()
print(f"Você tem {gil_atual} gil. Após o teleport, restam, {gil_restante}, gil.")