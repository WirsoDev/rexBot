from discord.ext import commands
import random
import wikipedia
import time
from NAV_FILES import dc_tc, dc_models, dc_cod_models, tc_to_cod
from BIBREVS import tecidos
from MODELOS_AQUINOS import modelos_aquinos_inv
import xlrd
import os
from my_funcs import weeknum
from . import tokan

t = time.ctime()

client = commands.Bot(command_prefix='!')


frases_modelos = ['! Bela merda de modelo!!', '! Este modelo é bem bonito!!',
                  '! Qualidade americana este modelo!!', '! Jasus...nem digo nada!!',
                  '! Mas isto vai dar em alguma coisa??', '! Isto é um sofa??', '! :D :D :D :D JASUS!!!']


gifs_rex = ['https://tenor.com/view/dinosaur-trex-summersault-boom-running-gif-9694162',
            'https://tenor.com/view/trex-horse-soccer-what-the-heck-wtf-gif-5080299',
            'https://tenor.com/view/rex-snow-snow-shovel-gif-15013849','https://tenor.com/view/trex-arms-gif-7622211']


users_aquinos = ('Wirso','Mrs. Jenni', 'Sandro')


@client.event
async def on_ready():
    print('='*80)
    print(f'O rex esta online!! At {t}')
    print('='*80)
    channel = client.get_channel(465868403014500363)
    await channel.send(f'I´m Online bitches\n {random.choice(gifs_rex)}')



@client.command()
async def wiki(ctx, *, question):
    '''

    '''
    lang = str(question[-2:]).strip().lower()
    procura = (question[:-2])
    try:
        if lang == 'pt':
            await ctx.send(f'{procura}? Espera uma beca, deixa procurar o significado disso em português!\n{" "} ')
        elif lang == 'en':
            await ctx.send(f'{procura}? Espera uma beca, deixa procurar o significado disso em inglês!\n{" "} ')
        elif lang == 'fr':
            await ctx.send(f'{procura}? Espera uma beca, deixa procurar o significado disso em francês!\n{" "} ')
        elif lang != 'PT' and lang != 'FR' and lang != 'EN':
            lang = 'PT'
            procura = question
            await ctx.send(f'{procura}? Espera uma beca, deixa procurar o significado disso em Português!\n{" "} ')
        wikipedia.set_lang(lang)
        sug = wikipedia.search(procura, results=3)
        print(f'Procura feita por {ctx.author.name} at {t}')
        print(sug)
        if (len(sug)) <= -1:
            await ctx.send('Sorry!')
        elif (len(sug)) >= 0:
            response = wikipedia.summary(sug[0])
            response_2 = response[:1500]
            await ctx.send(f'Ora bem, deve ser isto:\n{response_2}')
    except:
        await ctx.send('Man, mas isso é alguma coisa que se procure! Não encontrei nada...tenta ser mais espicífico!')


@client.command()
async def rev(ctx, *, content):
    if ctx.author.name in users_aquinos:
        print(f'On !rev : {ctx.author.name} at {t} -- {content}')
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


@client.command()
async def cod(ctx, *, content):
    if ctx.author.name in users_aquinos:
        print(f'On !cod : {ctx.author.name} at {t} -- {content}')
        content = content.upper().strip()
        frases_modelos_ramd = random.choice(frases_modelos)
        if content in dc_models:
            await ctx.send('Esse é o modelo ' + dc_models[content] + frases_modelos_ramd)
        else:
            await ctx.send(f'Humm...parece que não ha nada disso por aqui {ctx.author.name}.\n'
                           f'Esse codigo não deve estar criado!')
    else:
        await ctx.send(f'Sorry {ctx.author.name}, mas não tens competencia para usar um comando deste calibre!')


@client.command()
async def mod(ctx, *, content):
    if ctx.author.name in users_aquinos:
        print(f'On !mod : {ctx.author.name} at {t} -- {content}')
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
async def todos(ctx):
    if ctx.author.name in users_aquinos:
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


@client.command()
async def open():
    os.startfile('\\\\STORAGE\\Creative\\DESENVOLVIMENTO\\REGISTO GERAL DE DESENVOLVIMENTOS.xlsx')


@client.command()
async def week(ctx):
    await ctx.send(f'Estás na semana {weeknum()}')


@client.command()
async def gama(ctx, *,content):
    print(f'On !gama : {ctx.author.name} at {t} -- {content}')
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
