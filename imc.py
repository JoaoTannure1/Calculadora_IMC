def calcular_imc():
    print("Calculadora de IMC")
    
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "ABAIXO DO PESO"
    elif 18.5 <= imc < 25:
        classificacao = "PESO NORMAL"
    elif 25 <= imc < 30:
        classificacao = "SOBREPESO"
    elif 30 <= imc < 35:
        classificacao = "OBESIDADE GRAU I"
    elif 35 <= imc < 40:
        classificacao = "OBESIDADE GRAU II"
    else:
        classificacao = "OBESIDADE GRAU III (MÓRBIDA)"
    
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

calcular_imc()