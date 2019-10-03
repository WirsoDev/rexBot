import xlrd

tc_file = ('G:\\python\\REX\\NAV_DATA\\TC.xlsx')#Path of xlr file
models_file = ('G:\\python\\REX\\NAV_DATA\\MODELOS.xlsx')


open_tc_file = xlrd.open_workbook(tc_file)
sheet_tc = open_tc_file.sheet_by_index(0)
open_models_file = xlrd.open_workbook(models_file)
sheet_models = open_models_file.sheet_by_index(0)

act_tc = sheet_tc.cell_value(1, 0)[16:]
act_models = sheet_models.cell_value(1, 0)[21:]

print(f'Base de dados TC atualizada a {act_tc}\n'
      f'Base de dados Models atualizada a {act_models}')

dc_tc = {}
dc_models = {}
dc_cod_models = {}
tc_to_cod = {}

#tecidos
for n in range(sheet_tc.nrows):
    cod = sheet_tc.cell_value(n, 1)
    price = sheet_tc.cell_value(n, 3)
    m2 = sheet_tc.cell_value(n, 8)
    desc = sheet_tc.cell_value(n, 2)
    dc_tc[cod] = f'{desc}  ---  {price}€/m  ---  {m2}m/lin em stock  |  Atualizado a {act_tc}'


#codigo/modelo and modelo/codigo
for m in range(sheet_models.nrows):
    cod_model = sheet_models.cell_value(m,0)
    name_model = sheet_models.cell_value(m, 1)
    dc_models[cod_model] = name_model
    dc_cod_models[name_model] = cod_model

#codigo nav - cod tec
for itens in range(sheet_tc.nrows):
    cod1 = sheet_tc.cell_value(itens, 0)
    cod2 = sheet_tc.cell_value(itens, 1)
    tc_to_cod[cod2] = cod1

