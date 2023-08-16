import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#ativação
@client.event
async def on_ready():
    print(f'{client.user} está online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!help'):
        print('Tente digitar: [!exercicio1],[!exercicio2], [!exercicio3] e [!exercicio4]')
    
    #boas vindas
    async def entrada(member):
        canal_principal = client.get_channel(1139633738653913149)
        mensagem = f'Bem vindo ao servidor, {member.mection}!'
        await canal_principal.send(mensagem)  

    #primeiro exercício
    if message.content.startswith('!exercicio1'):
        try:
            _, salario_str, valor_financiamento_str = message.content.split()
            salario = float(salario_str)
            valor_financiamento = float(valor_financiamento_str)

            if valor_financiamento <= 5 * salario:
                mensagem = "Financiamento concedido."
            else:
                mensagem = "Financiamento negado."

            print('Obrigado por nos consultar')

            await message.channel.send(mensagem)
        except ValueError:
            await message.channel.send("Formato inválido. Use: !exercicio1 <salario> <valor_financiamento>")

    if message.content.startswith('!exercicio2'):
        try:
            _, temp_carroUm_str, dist_carroUm_str, temp_carroDois_str, dist_carroDois_str = message.content.split()
            temp_carroUm = float(temp_carroUm_str)
            dist_carroUm = float(dist_carroUm_str)
            temp_carroDois = float(temp_carroDois_str)
            dist_carroDois = float(dist_carroDois_str)
            vel_media = dist_carroUm/temp_carroUm
            vel_mediaDois = dist_carroDois/temp_carroDois

            if vel_mediaDois< vel_media:
                mensagem=(f'A velocidade maior é do segundo carro com: {vel_mediaDois:.2f}')
            elif(vel_media==vel_mediaDois):
                mensagem=('Os dois carros possuem as mesmas velocidades médias')
            elif(vel_media>vel_mediaDois):
                mensagem = ('A velocidade do carro um é superior com: {vel_media:.2f}')

            await message.channel.send(mensagem)
        except ValueError:
            await message.channel.send("Formato inválido. Use: !exercicio2 <temp 1> <distancia 1> <temp 2> <distancia 2>")

    if message.content.startswith('!exercicio3'):
        try:
            _, nome_um_str, idade_um_str, nome_dois_str, idade_dois_str, ano_atual_str = message.content.split()
            nome_um = (nome_um_str)
            idade_um = int(idade_um_str)
            nome_dois = (nome_dois_str)
            idade_dois = int(idade_dois_str)
            ano_atual = int(ano_atual_str)

            calculo_ano_um = ano_atual-idade_um
            calculo_ano_dois = ano_atual-idade_dois

            if(idade_um>idade_dois):
                mensagem = (f'A pessoa mais nova é a {nome_dois} em: {calculo_ano_dois}')
            elif(idade_um<idade_dois):
                mensagem = (f'A pessoa mais nova é a {nome_um} nascida em: {calculo_ano_um}') 
            elif(idade_um==idade_dois):
                mensagem = (f'A {nome_um} e {nome_dois} possuem as mesmas idades nascidas em: {calculo_ano_um}')

            await message.channel.send(mensagem)
        except ValueError:
            await message.channel.send("Formato inválido. Use: !exercicio3 <nome 1> <idade 1> <nome 2> <idade 2> <ano atual>")

    if message.content.startswith("!exercicio4"):
        try:
            _, numero_um_str, numero_dois_str, numero_tres_str = message.content.split()
            numeros = [int(numero_um_str), int(numero_dois_str), int(numero_tres_str)]
            numeros_ordenados = sorted(numeros)
            print(numeros_ordenados)
            mensagem = f'O maior numero é: {numeros_ordenados[2]}'
            await message.channel.send(mensagem)
        except ValueError:
            await message.channel.send("Formato inválido. Use: !exercicio4 <numero 1 > <numero 2> <numero 3>")

client.run('TOKEN')
