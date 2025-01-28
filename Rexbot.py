# main program


__title__ = 'rexbot'
__author__ = 'Wirso'
__copyright__ = 'Copyright 2020 wirso'
__version__ = '1.3.0 - hotfix 1'
__github__ = 'https://github.com/WirsoDev/rexBot'


from discord.ext import commands, tasks
import discord
import random
import time
from datetime import datetime, timedelta
import xlrd
from tokan import tokan
from db.database import aquinosusers, dbtecidos, accepthours_metalapi
from external_api.names import Getnames
from external_api.music import Metalinj
from functions import rexgifs, weeknum, aqpassgen, Dict_tecidos, Dict_modelos, resize_img, facts, weekday
from whatermark import apply_water_mark
#from remove_bg import remove_bg
from embed import Rexembed
from docs.news_v1_2 import title_main, descrição_main, title_hf1, descrição_htf1, footer_ht1
from prognews import get_last_url, prog_controller
import sys
import argparse
from feets import FEETS
import os
from PIL import Image
import fitz
from llm import Rexllm
import threading
from flask import Flask, request, jsonify
import asyncio
from functools import partial

app = Flask(__name__)


# init cliente
client = commands.Bot(command_prefix=['.', '!'], intents=(discord.Intents.all()))

# channels
channels = {
    'music': 463277986636890132,
    'rex': 585752207501033472,
    'rexnews': 669219347339673630,
    'zezign': 655087818040672266,
    'DRS': 1327230311041335357,
}


def excel_number_to_date(excel_number):
    # Excel's date system starts from December 30, 1899
    excel_start = datetime(1899, 12, 30)
    
    # Add the number of days to the start date
    date = excel_start + timedelta(days=excel_number)
    
    # Format the date as dd/mm/yyyy
    return date.strftime('%d/%m/%Y')


#api routes
@app.route('/', methods=['GET'])
def mainroute():
    return jsonify({'status': 'OK'})


# Create a function to send Discord message asynchronously
async def send_discord_message(channel, embed):
    await channel.send(embed=embed)

# Modified Flask route
@app.route('/newtask', methods=['POST'])
def newtask():
    data = request.get_json()

    if data:

        #convert deadline to datetime object (if recived 45671/time stamp else dont convert)
        if type(data['deadline']) == int or type(data['deadline']) == float:
            data['deadline'] = excel_number_to_date(data['deadline'])

        if isinstance(data['modelCode'], (int, float)):
            modelCode = int(data['modelCode'])
        else:
            modelCode = None

        try:
            if data['issue_id']:
                add_jira = 'and added to Jira!'
                link = f'https://aquinosdev.atlassian.net/jira/core/projects/DM/board?selectedIssue={data["issue_id"]}'
                thumbnail='https://cdn.discordapp.com/attachments/585752207501033472/1333721874730975294/stsmall845x845-pad1000x1000f8f8f8.jpg?ex=6799ecca&is=67989b4a&hm=d5f438cca2e6621104b638949f7f86817709ef913372a3a12423c3c801e9cbf9&'
            else:
                add_jira = ''
                link = ''
                thumbnail=''
        except KeyError:
            add_jira = ''
            link = ''
            thumbnail=''


        msg = f'''
        Code: {modelCode}
        Model: {data['modelName'] or None}
        Element: {data['tipologia'] or None}
        Request: {data['tiposPedido']}
        {link}
        '''
        # Log data
        print(f'Received data: {data}')

        # Log channel retrieval
        channel = client.get_channel(channels['DRS'])
        print(f'Channel: {channel}')

        if channel:
            # Create the embed
            embed = Rexembed(
                title=f'DRS {data["drsNumber"]} created {add_jira}',
                description=msg,
                colour='blue',
                thumbnail=thumbnail
            ).normal_embed()
            
            # Schedule the coroutine to run
            asyncio.run_coroutine_threadsafe(
                send_discord_message(channel, embed),
                client.loop
            )
            print('Message sent task created!')
        else:
            print('Channel not found or bot does not have access.')

        return jsonify(data)
    else:
        print('Invalid data received.')
        return jsonify({'status': 'error'}), 400


@client.event
async def on_ready():
    #prognews.start()
    print('='*80)
    print(f'Rex Online!! At {time.ctime()}')
    print('='*80)

    

@tasks.loop(minutes=10)
async def prognews():

    data = get_last_url()
    controller = prog_controller()
    channel = client.get_channel(channels['music'])
    
    if controller == False:
        await channel.send(data)
        print('Run ProgNews - Prog news on discord')
        txt = open('external_api/logs/prognews_controller.txt', 'w')
        txt.write(data)
        txt.close()
    return 

# main commands


@client.command()
async def size(ctx, *, c_arg):
    '''Redimensiona uma lista de imagens para o tamanho
       que pretendemos.

       Argumentos obrigatorios -> caminho para a pasta na rede + tamanho em px

       Comando: !size <caminho na rede>, <valor>

       Ex: !size \\STORAGE\Creative\Projetos\SHOWROOM_PRIVE\CAMPANHA_2\FICHEIROS_FINAIS\ANDREIA\FOTOS, 1000

       ATENÇÃO: Depois do caminho usar a , e depois o valor para o tamanho pretendido

    '''
    new_input = str(c_arg).split(',')
    path = new_input[0]
    size = int(new_input[1])
    await ctx.send(embed=Rexembed('Processing...', colour='Blue').normal_embed())
    try:
        await ctx.send(embed=Rexembed(f'{resize_img(path, size)} images successfully resized ', colour='blue').normal_embed())
    except:
        await ctx.send(embed=Rexembed('Hey, something go wrong!', colour='Red').normal_embed())


@client.command()
async def rev(ctx, *, rev):
    print(f'Run rev with {rev} by {ctx.author}')
    listItems = rev.split(' ')
    for item in listItems:
        rev = item.strip().upper()
        try:
            tecido = Dict_tecidos(rev)
            if tecido.descrição() == '':
                if tecido.preço() == 0:
                    await ctx.send(embed=Rexembed(dbtecidos[rev], f'{rev} | Sem stock - € não disponivel', 'green').normal_embed())
                else:
                    await ctx.send(embed=Rexembed(dbtecidos[rev], f'{rev} | {tecido.metros()} em stock - {tecido.preço()}€', 'green').normal_embed())
            else:
                if tecido.preço() == 0:
                    await ctx.send(embed=Rexembed(tecido.descrição(), f'{rev} | Sem stock - € não disponivel', 'green').normal_embed())
                else:
                    await ctx.send(embed=Rexembed(tecido.descrição(), f'{rev} | {tecido.metros()} em stock - {tecido.preço()}€', 'green').normal_embed())

        except KeyError:
            await ctx.send(embed=Rexembed('Go fish!    :fishing_pole_and_fish: ', colour='red').normal_embed())

    
@client.command()
async def gama(ctx, *, rev):
    '''Lista todos os revestimentos da gama. 

       Argumento obrigatório -> Nome da gama do revestimento

       Exemplo: !gama boston -> Boston Black - G0601, Boston SKY - G0621, ...
    '''
    print(f'Run !gama with {rev} by {ctx.author}')
    try:
        revestimento = Dict_tecidos(rev)
        if len(revestimento.gamas()[0]) == 0:
            await ctx.send(embed=Rexembed('Go fish!   :fishing_pole_and_fish: ', colour='red').normal_embed())
        else:
            #for itens in revestimento.gamas():
            #    await ctx.author.send(embed=Rexembed(description=itens, colour='blue').normal_embed())
            await ctx.send(embed=Rexembed(title=f'{rev.upper()} - {revestimento.gamas()[1]} colors' , description=revestimento.gamas()[0], colour='blue').normal_embed())
            #await ctx.send(embed=Rexembed(title='Done!!', colour='green', description='Revestimentos enviados por MP! ;)').normal_embed())

    except KeyError:
        await ctx.send(embed=Rexembed('Go fish!    :fishing_pole_and_fish: ', colour='red').normal_embed())


@client.command()
async def week(ctx):
    '''Retorna o numero da semana actual

       Não tem argumentos obrigatórios 

       Exemplo: !week 
    '''
    await ctx.send(embed=Rexembed(f'Estás na semana {weeknum()}. Seu burro!!', colour='blue').normal_embed())
    await ctx.send('https://tenor.com/view/shake-my-head-james-dutton-tim-mcgraw-1883-smh-gif-24993082')

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

    print(f'Run !genpass by {ctx.author}')
    password = aqpassgen(ctx)
    await ctx.author.send(embed=Rexembed(f'Pass gerada:', f'{password}', colour='green').normal_embed())
    time.sleep(0.2)
    await ctx.send(embed=Rexembed(f'A tua pass foi gerada e enviada por MP!', colour='blue').normal_embed())



@client.command()
async def feet(ctx, *, filter_):
    print(f'feets: filter {filter_} by {ctx.author}')

    accepted_filters = ['-c', '-m', '-ma']
    if filter_.split(' ')[0] not in accepted_filters:
        await ctx.send(embed=Rexembed('😒', 'Filters: -c / -m / -a / -ma', colour='red').normal_embed())
        return

    conn = FEETS()

    # Filter data
    if filter_.split(' ')[0] == '-c':
        code = filter_.split(' ')[1]
        data = conn.filter_data(code=code)

        if len(data) == 1:
            pdf_file_path = data[0]['pdf_file']
            pdf_document = fitz.open(pdf_file_path)
            first_page = pdf_document.load_page(0)
            pix = first_page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            image_path = 'output_image.jpg'
            image.save(image_path, 'JPEG')
            await ctx.send(
                embed=Rexembed(f"Material: {data[0]['material']} | Altura: {data[0]['altura']}mm", f'Pé {data[0]["codigo"]}', 'green').normal_embed()
            )
            await ctx.send(file=discord.File(image_path))
            os.remove(image_path)
    
    if filter_.split(' ')[0] == '-a':
        altura = int(filter_.split(' ')[1])
        data = conn.filter_data(altura=altura)
        if data:
            lines = ''
            for l in data:
                lines = lines + f'Pé {l['codigo']} | {l['material']}\n'

            await ctx.send(embed=Rexembed(title=f'{altura}mm feets:' , description=lines, colour='blue').normal_embed())
    
    if filter_.split(' ')[0] == '-m':
        material = (filter_.split(' ')[1])
        data = conn.filter_data(material=material)
        if data:
            lines = ''
            for l in data:
                lines = lines + f'Pé {l['codigo']} | {l['altura']}\n'

            await ctx.send(embed=Rexembed(title=f'Feets in {material}' , description=lines, colour='blue').normal_embed())

    if filter_.split(' ')[0] == '-ma':
        material = (filter_.split(' ')[1])
        altura = int((filter_.split(' ')[2]))
        data = conn.filter_data(material=material, altura=altura)
        if data:
            lines = ''
            for l in data:
                lines = lines + f'Pé {l['codigo']}\n'

            await ctx.send(embed=Rexembed(title=f'Feets in {material} and {altura}mm' , description=lines, colour='blue').normal_embed())


    return
    



@client.command()
async def modelo(ctx, *, codigo):
    '''Retorna o nome do modelo procurado.

       Argumento obrigatótio -> Codigo do modelo

       Exemplo: !modelo maxx -> 1017
    '''
    print(f'Run !modelo with {codigo} by {ctx.author}')
    try:
        modelo = Dict_modelos(codigo)
        await ctx.send(embed=Rexembed(f'{modelo.nome()}', colour='green').normal_embed())
    except KeyError:
        await ctx.send(embed=Rexembed('Codigo não é valido ou ainda não esta na base de dados! :/', colour='red').normal_embed())

@client.command()
async def hey(ctx, *prompt):
    prompt = " ".join(prompt)

    print(f'Run !hey with {prompt} by {ctx.author}')
    try:
        model = Rexllm()
        response = model.makeresponse(prompt, ctx.author)
        await ctx.send(response)
    except KeyError:
        await ctx.send(embed=Rexembed('Probs', colour='red').normal_embed())


@client.command()
async def imagine(ctx, *prompt):
    prompt = " ".join(prompt)

    print(f'Run imagine with {prompt} by {ctx.author}')
    try:
        model = Rexllm()
        response = model.makeresponse(prompt, ctx.author, noRex=True)
        await ctx.send(response)
    except KeyError:
        await ctx.send(embed=Rexembed('Probs', colour='red').normal_embed())


@client.command()
async def cod(ctx, modelo):
    '''Retorna o codigo do modelo procurado.

       Argumento obrigatótio -> Nome do modelo

       Exemplo: !modelo 1017 -> maxx
    '''
    print(f'Run !modelo with {modelo} by {ctx.author}')
    try:
        codigo = Dict_modelos(modelo)
        await ctx.send(embed=Rexembed(f'{codigo.codigo()}', colour='green').normal_embed())
    except KeyError:
        await ctx.send(embed=Rexembed('Nome do modelo não é valido ou ainda não esta na base de dados! :/', colour='red').normal_embed())



@client.command()
async def fact(ctx):
    '''Return a norris fact!'''
    print(f'Run a fact by {ctx.author}')
    await ctx.send(embed=Rexembed(title='Norris Fact:', description=facts(), colour='green', thumbnail='https://cdn.discordapp.com/attachments/519881712046702593/1213175072525652038/image.png?ex=65f48454&is=65e20f54&hm=a82d96537fff0c58ef2f1293b86e227da465f8008c867a50fff2c0be7cbac250&').normal_embed())

@client.command()
async def wm(ctx, *, args):

    args = args.split(',')
    path = False
    text = False
    resize = True

    if args[0]: 
        path = args[0] #path
        try:
            if args[1]: text = args[1]
        except IndexError:
            pass
        try:
            if args[2]: resize = False
        except IndexError:
            pass

        if path: print(path)
        if text: print(text)
        if resize: print(resize)
        await ctx.send(embed=Rexembed(title='Running', description="Working...", colour='green').normal_embed())
        func_result = apply_water_mark()

        await ctx.send(embed=Rexembed(title='Teste', description=args[0], colour='green').normal_embed())
    else:
        await ctx.send(embed=Rexembed(title='Error', description="Missing some args!", colour='red').normal_embed())

'''
@client.command()
async def rembg(ctx, c_arg):
    path = c_arg
    
    await ctx.send(embed=Rexembed(title='Finding images...', 
                                  description='Depending on the size of the images, this may take a while...',
                                  colour='Blue').normal_embed())
    try:
        await ctx.send(embed=Rexembed(f'Removed background from {remove_bg(path)} images', colour='blue').normal_embed())
    except:
        await ctx.send(embed=Rexembed(title='Hey, something go wrong!', 
                                      description='Remember that this command works on internal network paths only', 
                                      colour='Red').normal_embed())
'''
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


def run_flask():
    app.run(port=8080, debug=True, use_reloader=False)

# Run Flask in a separate thread
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

if __name__ == '__main__':
    client.run(tokan)
    
