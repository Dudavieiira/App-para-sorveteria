#Mensagem de boas vindas
print('---------------------------------------------------------------------------------------')
print('                 Olá, seja bem vindo(a) a sorveteria da Maria Eduarda!                 ')
print('---------------------------------------------------------------------------------------')

#Tabela com número de bolas e valores
print('---------------------------------------CARDÁPIO----------------------------------------')
print('N° DE BOLAS | SABORES TRADICIONAIS (tr) | SABORES PREMIUM (pr) | SABORES ESPECIAIS (es)')
print('     1      |          R$6,00           |        R$7,00        |         R$8,00        ')
print('     2      |          R$11,00          |        R$13,00       |         R$15,00       ')
print('     3      |          R$15,00          |        R$18,00       |         R$21,00       ')
acumulador = 0
while True: 
    sabor= input('Qual o sabor do sorvete (tr,pr,es): ')
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Opção inválida. Esse sabor de sorvete não existe.')
        continue #Se o usuário digitar algo inválido volta para o começo do while
   
    numero_bolas= input('Qual a quantidade de bolas de sorvete (1,2,3): ')
    if numero_bolas != '1' and numero_bolas != '2' and numero_bolas != '3':
        print('Opção inválida. Essa quantidade de bolas de sorvete não existe.')
        continue #Se o usuário digitar algo inválido volta para o começo do while
    
    if numero_bolas == '1' and sabor =='tr':
        print('Você escolheu 1 bola de sorvete do sabor TRADICIONAL')
        acumulador = acumulador + 6 #pegue o valor do acumulador e some com 6
    elif numero_bolas == '2' and sabor =='tr':
        print('Você escolheu 2 bola de sorvete do sabor TRADICIONAL')
        acumulador = acumulador + 11 #pegue o valor do acumulador e some com 11
    elif numero_bolas == '3' and sabor =='tr':
        print('Você escolheu 3 bola de sorvete do sabor TRADICIONAL')
        acumulador = acumulador + 15 #pegue o valor do acumulador e some com 15
    elif numero_bolas == '1' and sabor =='pr':
        print('Você escolheu 1 bola de sorvete do sabor PREMIUM')
        acumulador = acumulador + 7 #pegue o valor do acumulador e some com 7
    elif numero_bolas == '2' and sabor =='pr':
        print('Você escolheu 2 bola de sorvete do sabor PREMIUM')
        acumulador = acumulador + 13 #pegue o valor do acumulador e some com 13
    elif numero_bolas == '3' and sabor =='pr':
        print('Você escolheu 3 bola de sorvete do sabor PREMIUM')
        acumulador = acumulador + 18 #pegue o valor do acumulador e some com 18
    elif numero_bolas == '1' and sabor =='es': 
        print('Você escolheu 1 bola de sorvete do sabor ESPECIAL')
        acumulador = acumulador + 8 #pegue o valor do acumulador e some com 8
    elif numero_bolas == '2' and sabor =='es':
        print('Você escolheu 2 bola de sorvete do sabor ESPECIAL')
        acumulador = acumulador + 15 #pegue o valor do acumulador e some com 15
    elif numero_bolas == '3' and sabor =='es':
        print('Você escolheu 3 bola de sorvete do sabor ESPECIAL')
        acumulador = acumulador + 21 #pegue o valor do acumulador e some com 21
    
    pedir_mais= input('Deseja pedir mais algum sorvete? (S/N): ')
    if pedir_mais.upper() == 'S': #resolve o problema de digitar 's' e 'S' ou 'n' e 'N'
        continue
    else: 
        print('O valor total a ser pago é: R${:.2f}' .format(acumulador))
        print('---------------------------------------------------------------------------------------')
        print('          Obrigado por compra na sorveteria da Maria Eduarda, volte sempre!            ')
        print('---------------------------------------------------------------------------------------')
        break





