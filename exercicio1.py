basemaior = float(input("Digite o tamanho da base maior do seu Trapézio:\n"))
basemenor = float(input("Digite o tamanho da base menor do seu Trapézio:\n"))
altura = float(input("Digite a Altura do seu Trapézio:\n"))

somabase = basemaior+basemenor

soma = somabase * altura/2

print(f"A base do seu trapézio é de:\n%2.f" %(soma))
