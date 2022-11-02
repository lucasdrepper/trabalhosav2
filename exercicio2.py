taxa_imposto = float(input("Qual a porcentagem de imposto sobre o produto?\n"))
custo = float(input("Quanto custa o produto?\n"))

imposto = custo / taxa_imposto

custo = custo + imposto

print(f"O valor do seu produto com impostos será de\n%2.f" %(custo))
