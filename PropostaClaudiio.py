import math
import os


Xa = int(input('Digite o valor para Xa: '))
Ya = int(input('Digite o valor para Ya: '))

print('A posição de A é (', Xa , ',', Ya , ')?')
confirmacao = input('[s/n]')

os.system('cls')

if confirmacao == 's':
    a = int(input("Digite o valor de 'a' da equação da reta: "))
    b = int(input("Digite o valor de 'b' da equação da reta: "))
    c = int(input("Digite o valor de 'c' da equação da reta: "))

    print('(',a,'x²)+ (',b,'x) + (',c,')= 0')
    confirmacao2 = input('[s/n]')
    
    os.system('cls')
    
    if confirmacao2 == 's':
        dividendo = abs(a*Xa + b*Ya + c)
        divisor = math.sqrt(a**2 + b**2)
        
        distancia = dividendo / divisor
        
        print("A distância do ponto A(",a,",",b,") à reta r((",a,"x²) + (",b,"x ) + (",c,")= 0) é de: ", distancia)
        input()
    elif confirmacao2 == 'n':
        print("Reinicie o programa e insira os dados novamente!")
        input()
    else:
        print('Opção inválida!')
        input()
elif confirmacao == 'n':
    print("Reinicie o programa e insira os dados novamente")
    input()
else:
    print('Opção inválida!')
    input()