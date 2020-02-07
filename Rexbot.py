# main program 


__title__ = 'rexbot'
__author__ = 'Wirso'
__copyright__ = 'Copyright 2020 wirso'
__version__ = '1.2.0 - hotfix 1'
__github__ = 'https://github.com/WirsoDev/rexBot'


from discord.ext import commands, tasks
import discord
import random
import wikipedia
import time
from datetime import datetime
import xlrd
from tokan import tokan
from db.database import aquinosusers, dbtecidos, accepthours_metalapi
from external_api.names import Getnames
from external_api.music import Metalinj
from functions import rexgifs, weeknum, aqpassgen, Dict_tecidos, Dict_modelos
from embed import Rexembed
from docs.news_v1_2 import title_main, descrição_main, title_hf1, descrição_htf1, footer_ht1


# init cliente
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    #event Metalinjection news
    getmusic.start()
    print('='*80)
    print(f'O rex esta online!! At {time.ctime()}')
    print('='*80)

    # channel_news = client.get_channel(669219347339673630)
    # await channel_news.send(embed=Rexembed(
    #    title=title_hf1,
    #   description=descrição_htf1,
    #   footer=footer_ht1,
    #   thumbnail='https://cdn.discordapp.com/attachments/585752207501033472/669229075088277517/updates-01-01.png',
    #   colour='blue'
    #).normal_embed())


# events and tasks


@tasks.loop(hours=5)
async def getmusic():
    time = datetime.now()
    hour = str(time.time())[0:2]
    week = datetime.datetime.weekday(time)
    if week == 0 and hour in accepthours_metalapi:
        channel = client.get_channel(585752207501033472)
        news = Metalinj()
        count = len(news.bandsname())
        index = 0
        index_2 = 0
        while count >= 0:
            try:
                await channel.send(embed=Rexembed(
                    title=news.bandsname()[index],
                    image=news.imagelink()[index],
                    description= f'{news.description()[index_2]}\n  \n{news.description()[index_2 + 1]}',
                    colour='blue'
                ).normal_embed())
                await channel.send(news.youtube()[index])
                index += 1
                index_2 += 3
                count -= 1
            except IndexError:
                pass
                break
        await channel.send('@everyone novidades da semana!')


@client.command()
async def version(ctx):
    '''Versão atual do Rex'''
    await ctx.send(embed=Rexembed(title_main, descrição_main, colour='blue').normal_embed())


#main commands


@client.command()
async def rev(ctx, *, rev):
    '''Procura informações de revestimentos aquinos.

        . Nome
        . quantidade em stock
        . preço por metro
       
       Argumento obrigatório -> Codigo de revestimento
       
       Exemplo: !rev c1758 -> Zenith 606 ...
       
       '''
    rev = rev.strip().upper()
    try:
        tecido = Dict_tecidos(rev)
        if tecido.descrição() == '':
            if tecido.preço() == 0:
                await ctx.send(embed=Rexembed(dbtecidos[rev], 'Sem stock - € não disponivel', 'green').normal_embed())
            else:
                await ctx.send(embed=Rexembed(dbtecidos[rev], f'{tecido.metros()} em stock - {tecido.preço()}€', 'green').normal_embed())
        else:
            if tecido.preço() == 0:
                await ctx.send(embed=Rexembed(tecido.descrição(), 'Sem stock - € não disponivel', 'green').normal_embed())
            else:
                await ctx.send(embed=Rexembed(tecido.descrição(), f'{tecido.metros()} em stock - {tecido.preço()}€', 'green').normal_embed())

    except KeyError:
        await ctx.send(embed=Rexembed('Codido não é valido ou não foi encontrado na base de dados :/', colour='red').normal_embed())


@client.command()
async def gama(ctx, *, rev):
    '''Lista todos os revestimentos da gama. 

       Argumento obrigatório -> Nome da gama do revestimento

       Exemplo: !gama boston -> Boston Black - G0601, Boston SKY - G0621, ...
    '''
    try:
        revestimento = Dict_tecidos(rev)
        if len(revestimento.gamas()) == 0:
            await ctx.send(embed=Rexembed('Revestimento não encontrado! :/', colour='red').normal_embed())
        else:
            for itens in revestimento.gamas():
                await ctx.send(embed=Rexembed(description=itens, colour='blue').normal_embed())

            await ctx.send(embed=Rexembed('Done!!', colour='green').normal_embed())
    
    except KeyError:
        await ctx.send(embed=Rexembed('Revestimento não encontrado! :/', colour='red').normal_embed())



@client.command()
async def week(ctx):
    '''Retorna o numero da semana actual

       Não tem argumentos obrigatórios 

       Exemplo: !week 
    '''
    await ctx.send(embed=Rexembed(f'Estás na semana {weeknum()}', colour='blue').normal_embed())


@client.command()
async def genpass(ctx, *, givenname=''):

    '''Gera uma pass aleatória de 10 caracteres dentro das normas dos Aquinos
    Ignora caracteres no nome do utilizador caso o givenname não seja atribuido.

    A pass é enviada por mensagem privada.

    Exemplo: !genpass - Returns: qC/T40dQ#5 
    Caracteres ignorados: w, i, l, s, o, n

    Exemplo 2: !genpass wilsonmarques - Returns: qC/T40dQ#5
    Caracteres ignorados: w, i, l, s, o, n, m, a, r, q, e

    Boa sorte a decorar isto! :D'''

    password = aqpassgen(ctx)
    await ctx.author.send(embed=Rexembed(f'Pass gerada:', f'{password}', colour='green').normal_embed())
    time.sleep(0.2)
    await ctx.send(embed=Rexembed(f'A tua pass foi gerada e enviada por MP!', colour='blue').normal_embed())


@client.command()
async def nomes(ctx, *, types=''):
    '''Cria uma lista de 5 nomes random.

    Não tem argumentos obrigatórios

    Exemplo: !nomes -> Benji, Caiden, Paul, ...
    '''
    listnames = Getnames(types)
    names = listnames.getnames()[:5]

    await ctx.send(embed=Rexembed(description=f'{names[0]}\n{names[1]}\n{names[2]}\n{names[3]}\n{names[4]}', colour='green').normal_embed())


@client.command()
async def modelo(ctx, *, codigo):
    '''Retorna o nome do modelo procurado.

       Argumento obrigatótio -> Codigo do modelo

       Exemplo: !modelo maxx -> 1017
    '''
    try:
        modelo = Dict_modelos(codigo)
        await ctx.send(embed=Rexembed(f'{modelo.nome()}', colour='green').normal_embed())
    except KeyError:
        await ctx.send(embed=Rexembed('Codigo não é valido ou ainda não esta na base de dados! :/', colour='red').normal_embed())


@client.command()
async def cod(ctx, modelo):
    '''Retorna o codigo do modelo procurado.

       Argumento obrigatótio -> Nome do modelo

       Exemplo: !modelo 1017 -> maxx
    '''
    try:
        codigo = Dict_modelos(modelo)
        await ctx.send(embed=Rexembed(f'{codigo.codigo()}', colour='green').normal_embed())
    except KeyError:
        await ctx.send(embed=Rexembed('Nome do modelo não é valido ou ainda não esta na base de dados! :/', colour='red').normal_embed())


# fun stuff

@client.event
async def on_message(message):
    author = message.author.name
    chibeles = ('chibeles', 'belito', 'andre chibeles', 'andré chibeles')
    if message.content.lower().startswith(chibeles):
        await message.channel.send('https://tenor.com/view/john-travolta-lost-gif-10251428')
    if message.content.lower().startswith('ovelha'):
        await message.channel.send(f'Uma ovelhinha para o rex...obrigado {author}!!\nAonde meto os ossos? :)')
    await client.process_commands(message)


if __name__ == '__main__':
    client.run(tokan)
