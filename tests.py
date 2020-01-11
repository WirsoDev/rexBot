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


import xlrd

class Dict_modelos:
    def __init__(self, cod):
        modelos = (r'EXCEL LIBS/MODELOS.xlsx')
        self.sheet_modelos = xlrd.open_workbook(modelos).sheet_by_index(0)
        self.cod = cod.strip().upper()

    
    def nome(self):

        dic_modelos = {}

        for n in range(self.sheet_modelos.nrows):
            codigo = self.sheet_modelos.cell_value(n, 0)
            nome = self.sheet_modelos.cell_value(n, 1)
            dic_modelos[codigo] = (nome)
        
        return dic_modelos[self.cod]

    def codigo(self):

        dic_codigo = {}

        for n in range(self.sheet_modelos.nrows):
            nome = self.sheet_modelos.cell_value(n, 1)
            codigo = self.sheet_modelos.cell_value(n, 0)
            dic_codigo[nome] = (codigo)

        return dic_codigo[self.cod]


if __name__ == "__main__":
    modelo = Dict_modelos('079')
    codigo = Dict_modelos('nevada')

    print(modelo.nome())
    print(codigo.codigo())




