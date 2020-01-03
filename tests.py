import xlrd


class Dict_tecidos:

    def __init__(self, rev):

        tecidos = (r'EXCEL LIBS/TC_02.xlsx')
        self.sheet_tecidos = xlrd.open_workbook(tecidos).sheet_by_index(0)
        self.rev = rev.strip().upper()



    def descrição(self):

        dic_descrição = {}

        for n in range(self.sheet_tecidos.nrows):
            codigo = self.sheet_tecidos.cell_value(n, 2)
            descrição = self.sheet_tecidos.cell_value(n, 3)
            dic_descrição[codigo] = (descrição)

        return dic_descrição[self.rev]


    def preço(self):

        dic_preço = {}

        for n in range(self.sheet_tecidos.nrows):
            codigo = self.sheet_tecidos.cell_value(n, 2)
            preço = self.sheet_tecidos.cell_value(n, 11)
            dic_preço[codigo] = (preço)

        return dic_preço[self.rev]


    def metros(self):

        dic_metros = {}

        for n in range(self.sheet_tecidos.nrows):
            codigo = self.sheet_tecidos.cell_value(n, 2)
            metros = self.sheet_tecidos.cell_value(n, 16)
            dic_metros[codigo] = (metros)

        return dic_metros[self.rev]





if __name__ == "__main__":
    tecido = Dict_tecidos(rev)


    








