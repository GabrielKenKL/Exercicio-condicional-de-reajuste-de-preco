#algorítmo
print("Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:")

#declarar
print("Preço atual:")
PA = float(input())

print("Média mensal:")
M = float(input())

if PA < 30 and M < 500:
    PN = PA * 1.10
elif PA >= 30 and PA < 80 and M >= 500 and M < 1000:
    PN = PA * 1.15
elif PA >= 80 and M >= 1000:
    PN = PA * 0.95
else:
    PN = PA

print ("O preço novo seria de: R$" , f"{PN:.2f}")