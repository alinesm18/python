peso = float(input( "digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / (altura *2)

print(f"seu IMC é = {imc}")

if imc < 18.5:
    print ("sua classificação: abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print ("sua classificação: peso normal.")
elif 25 <= imc <= 34.9:
    print ("sua classificação: sobrepeso. ")
else:
    print ("sua classificação: obesidade.")