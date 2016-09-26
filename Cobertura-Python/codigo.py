# Paices y abreviatura
paises = {
    "Panama":"PA",
    "Colombia":"CO",
    "Ecuador":"EC",
    "Argentina":"AR"
}
# Abreviatura y codigo
codigo = {
    "PA":"+507",
    "CO":"+57",
    "EC":"+593",
    "AR":"+54"
}

print("Cobertura Internacional")
print("-"*23)
print("Lista de Paices " + str(paises.keys()))

x = input("\nEscriba el Nombre del Pais: ")
#if paises[x] != None:
print("\nEl prefijo telefonico de "+x+" ("+paises[x]+") es "+codigo[paises[x]]+".")

posibles = []
print("\nRecomendaciones:")
print("-"*15)
np = input("¿Que pais debemos darle cobertura? -> ")
posibles.append(np)
print("\n¡Gracias por su cooperación! Esperamos que "+posibles[0]+"sea incluido.")
#else:
#    print("Actualmente no tenemos cobertura en "+x+".")
