calcule = input('\nDigite a expressão que deseja calcular: => ')
if not calcule:
    print("Você não informou uma expressão válida!")
else:
    print("Resultado =", eval(calcule))
