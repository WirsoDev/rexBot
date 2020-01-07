from discord.ext import commands
import discord
import random
import wikipedia
import time
from NAV_FILES import dc_tc, dc_models, dc_cod_models
import xlrd
from tokan import tokan
from db.database import aquinosusers, dbtecidos, modelos_aquinos, modelos_aquinos_inv
from db.randomnames import Getnames
from functions import frasesmodelos, rexgifs, weeknum, aqpassgen, Dict_tecidos
from embed import Rexembed



client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('='*80)
    print(f'O rex esta online!! At {time.ctime()}')
    print('='*80)


@client.command()
async def version(ctx):
    '''Versão atual do Rex'''

    await ctx.send(embed=Rexembed('You are running rex version 1.2', colour='red').normal_embed())



@client.command()
async def rev(ctx, *, rev):
    rev = rev.upper().strip()
    tecido = Dict_tecidos(rev)
    if rev not in tecido.codigo():
        await ctx.send('ERROR')
    else:
        try:
            if tecido.descrição() == '':
                if rev in dbtecidos:
                    tecido_db = dbtecidos[rev]
                    await ctx.send(embed=Rexembed(tecido_db,
                    f'{tecido.metros()} metros em stock - {tecido.preço()}€', 'green').normal_embed())
                else:
                    await ctx.send(embed=Rexembed('ERRO: Codigo não valido', colour='red').normal_embed)
            else:
                await ctx.send(embed=Rexembed(tecido.descrição(),
                f'{tecido.metros()} metros em stock - {tecido.preço()}€', 'green').normal_embed())
        except:
            await ctx.send(embed=Rexembed('ERRO: Alguma coisa correu mal :/', colour='red').normal_embed)


'''
@client.command()
async def cod(ctx, *, content):
    if ctx.author.name in aquinosusers:
        print(f'On !cod : {ctx.author.name} at {time.ctime()} -- {content}')
        content = content.upper().strip()
        frases_modelos_ramd = random.choice(frasesmodelos)
        if content in dc_models:
            await ctx.send('Esse é o modelo ' + dc_models[content] + frases_modelos_ramd)
        else:
            await ctx.send(f'Humm...parece que não ha nada disso por aqui {ctx.author.name}.\n'
                           f'Esse codigo não deve estar criado!')
    else:
        await ctx.send(f'Sorry {ctx.author.name}, mas não tens competencia para usar um comando deste calibre!')
'''

@client.command()
async def mod(ctx, *, content):
    if ctx.author.name in aquinosusers:
        print(f'On !mod : {ctx.author.name} at {time.ctime()} -- {content}')
        content = content.upper().strip()
        if content in dc_cod_models:
            await ctx.send('Esse modelo é o ' + dc_cod_models[content])
        elif content not in dc_cod_models:
            if content in modelos_aquinos_inv:
                await ctx.send('Esse modelo é o ' + modelos_aquinos_inv[content])
            else:
                await ctx.send(f'Humm...parece que não ha nada disso por aqui {ctx.author.name}.\n'
                                   f'Esse codigo ainda não deve estar criado!')
    else:
        await ctx.send(f'Sorry {ctx.author.name}, mas não tens competencia para usar um comando deste calibre!')




@client.command()
async def week(ctx):
    '''Retorna o numero da semana actual'''
    await ctx.send(f'Estás na semana {weeknum()}')


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
    print(f'pass {password} gerada para {ctx.author.name}')
    await ctx.author.send(embed=Rexembed(f'Pass gerada:', f'{password}', colour='green').normal_embed())
    time.sleep(0.3)
    await ctx.send(f'A tua pass foi gerada e enviada por MP')

'''
@client.command()
async def gama(ctx, *,content):
    print(f'On !gama : {ctx.author.name} at {time.ctime()} -- {content}')
    key = content.strip()
    file = xlrd.open_workbook(r'\\STORAGE\Creative\DC_DOCS\LISTA DE REVESTIMENTOS_NAV.xlsx')
    work_sheet = file.sheet_by_index(0)
    rows = work_sheet.nrows
    key01 = key.lower().strip()
    key02 = key.upper().strip()
    key03 = key.capitalize().strip()
    list = []
    await ctx.send(':BETA TESTING:')
    if len(key) <= 0:
        pass
    else:
        for itens in range(rows):
            name = str(work_sheet.cell_value(itens, 1))
            cod = work_sheet.cell_value(itens, 2)
            if 'EUROFACTOR' not in name:
                if key01 in name:
                    list.append(f'{name} -- {cod}')
                elif key02 in name:
                    list.append(f'{name} -- {cod}')
                elif key03 in name:
                    list.append(f'{name} -- {cod}')
        for lines in list:
            await ctx.send(lines)
        await ctx.send(f'E é isso {ctx.author.name}! ')
'''


@client.command()
async def nomes(ctx, *, types='boy_names'):
    listnames = Getnames(types)
    names = listnames.getnames()[:4]
    await ctx.send(embed=Rexembed('Lista de nomes:',
    f'{names[0]}\n{names[1]}\n{names[2]}\n{names[3]}',
    'green'

    ).normal_embed())




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
