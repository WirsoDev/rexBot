from discord.ext import commands
import random
import wikipedia
import time
# from NAV_FILES import dc_tc, dc_models, dc_cod_models
from MODELOS_AQUINOS import modelos_aquinos_inv
import xlrd
from tokan import tokan
from db.database import aquinosusers, tecidos
from functions import frasesmodelos, rexgifs, weeknum, aqpassgen


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('='*80)
    print(f'O rex esta online!! At {time.ctime()}')
    print('='*80)


'''
@client.command()
async def rev(ctx, *, content):
    if ctx.author.name in aquinosusers:
        print(f'On !rev : {ctx.author.name} at {time.ctime()} -- {content}')
        content = str(content).strip().upper()
        if content in dc_tc:
            if dc_tc[content][0] == ' ':
                await ctx.send(f'{tecidos[content]}{dc_tc[content]}')
            else:
                await ctx.send(dc_tc[content])
        else:
            await ctx.send(f'Sorry {ctx.author.name}! Não encontro esse codigo!')
    else:
        await ctx.send(f'Sorry {ctx.author.name}, mas não tens competencia para usar um comando deste calibre!')
'''

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
'''

'''
@client.command()
async def todos(ctx):
    if ctx.author.name in aquinosusers:
        file_registos = xlrd.open_workbook('//STORAGE/Creative/DESENVOLVIMENTO/REGISTO GERAL DE DESENVOLVIMENTOS.xlsx')
        sheet = file_registos.sheet_by_index(0)
        rows = sheet.nrows
        estado = ('POR INICIAR', 'EM DESENVOLVIMENTO', '')
        if ctx.author.name == 'Wirso':
            atribuido = 'WILSON'
        elif ctx.author.name == 'Sandro':
            atribuido = 'SANDRO'
        elif ctx.author.name == 'Mrs. Jenni':
            atribuido = 'JENNIFER'
        await ctx.send(f'Deixa-me consultar aqui o almanaque {ctx.author.name}!')
        time.sleep(1)
        for n in range(rows):
            if sheet.cell_value(n, 7) == atribuido and sheet.cell_value(n, 2) in estado:
                id = sheet.cell_value(n, 0)
                deadline = sheet.cell_value(n, 11)
                descrição = sheet.cell_value(n, 4)
                await ctx.send(f' \n -{id} |  {descrição}  |   {deadline[8:]}\n ')
        await ctx.send('E pronto...é isto que tens para fazer!')
    else:
        await ctx.send('Man, vai pedir trabalho ao teu patrão!')
'''


@client.command()
async def week(ctx):
    await ctx.send(f'Estás na semana {weeknum()}')


@client.command()
async def genpass(ctx, *, name):

    '''Gera uma pass aleatória de 10 caracteres dentro das normas dos Aquinos
Ignora caracteres no nome do utilizador.

Exemplo: !genpass Wilson - Returns: qC/T40dQ#5

Boa sorte a decorar isto! :D'''


    print(f'pass {aqpassgen(name)} gerada para {ctx.author.name}')
    await ctx.author.send( f'Pass gerada: {aqpassgen(name)}')

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
