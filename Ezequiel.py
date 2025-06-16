false = pergunta = str(input(f"O'que deseja fazer?\ 1- Faz um pix \ n 2- Mostra o extrato \ n 3- deposita \ n 4- Saia do sistema \n digite o numero"))
valor = 0
if pergunta == 1:
    nome = input(f"para quem voce deseja fazer o pix?")
    valor = float(input(f"Qual o valor\n"))
    print(f"Pix de {valor} R$ feito com sucesso para {nome}")
elif pergunta ==2:
    saldo = 100
    extrato = saldo = valor
    print(f"Seu saldo é {saldo}R$")
elif pergunta ==3:
    deposito = float(input(f"Quanto você deseja colocar no deposito?"))
    print (f"Deposito de {deposito} R$ concluido")
else: 
    print(f"concluido")

    
                     


               