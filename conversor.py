def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def mettersToKm(metters):
    km = metters / 1000
    return km

x = 0;
#Agora, irei visualizar os resultados
while x != 3:
    print("Escolha uma opcaoo:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Metters para Km")    
    print("3 - Sair")
    x = int(input("Digite o numero da opcao desejada: "))

    if x == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsiusToFahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

    elif x == 2:
        metters = float(input("Digite a distancia em Metters: "))
        km = mettersToKm(metters)
        print(f"A distância em Km é: {km}Km")

    elif x == 3:
        print("Saindo do programa...")
    else:
        print("Opçao invalida. Tente novamente.")           
