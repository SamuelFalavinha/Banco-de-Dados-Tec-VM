#Ariane
print('Escolha a Temperatura em que se encontra:')
escala = (str(input('Digite C para celsius, F para Fahrenheit e K para Kelvin: ')))
temperatura = float(input('Qual o valor da temperatura na escala que você quer converter?: '))
conversao = str(input('Em queal escala está a temperatura para qual você quer converter?,usando C para Celsius,F para Fahrenheit e K para Kelvin: '))

#Samuel

if escala == 'F' and conversao == 'C':
  tempC = print(float('A temperatura em Celsius é: ', ( temperatura - 32) * 5/9 ))
  if tempC < 0.0:
    print('A água está em estado Sólido.')
  if tempC < 100.0:
    print('A água está em estado Líquido.')
  else:
    print('A água está em estado Gasoso.')

if escala == 'F' and conversao == 'K':
  tempK = print(float('A temperatura em Kelvin é: ', ( temperatura - 32) * 5/9 + 273,15),'K')
  if tempK < 273.15:
    print('A água está em estado Sólido.')
  if tempK < 373.15:
    print('A água está em estado Líquido.')
  else:
    print('A água está em estado Gasoso.')

#Evellyn
    
if escala == 'C' and conversão == 'K':
  tempK = print(float("A temperatura em Kelvin é:",(temperatura + 273,15),'K')
                
  if tempK < 273.15:
    print("A água está em estado Sólido")
  if tempK < 373.15:
    print("A água está em estado Líquido")
  else:
    print("A água está em estado Gasoso ")

if escala == "C" and conversão == 'F':
  tempF = print(float('A temperatura em Fahrenheit é:',( temperatura * 9/5) + 32)
if tempF < 459.0:
  print("A água está em estado Sólido ")
  if tempF < 212.0:
    print("A água está em estado Líquido ")
  else:
    print("A água está em estado Gasoso")

#Ranyele 

if escala == 'K' and conversao == 'C':
  tempK = print(float('A temperatura em Celsius é: ', (temperatura - 273,15))
  if tempK < 0.0:
   print('A água está em estado Sólido.')
  if tempK < 100.0:
    print('A água está em estado Líquido.')
  else:
    print('A água está em estado Gasoso.')

if escala == 'K' and conversao == 'F':
  tempK = print(float('A temperatura em Fahrenheit é: ', (temperatura - 273,15) * 9/5 + 32)
  if tempK < 459.0:
    print('A água está em estado Sólido.')
  if tempK < 212.0:
    print('A água está em estado Líquido.')
  else:
    print('A água está em estado Gasoso.')  
