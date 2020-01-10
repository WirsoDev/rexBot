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


'''
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


