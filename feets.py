import xlrd
import re


class FEETS:

    def __init__(self):

        feets_data = (r'\\storage\Gabinete Técnico\DESENHOS TECNICOS\REF-PÉS\BASE DADOS_REF_PÉS.xlsx')
        self.pdf_url = (r'\\storage\Gabinete Técnico\DESENHOS TECNICOS\REF-PÉS')
        self.sheet_feets = xlrd.open_workbook(feets_data).sheet_by_index(0)
        self.materials_dict = {
            'METAL': [
                'AÇO', 'AÇO ESCOVADO', 'AÇO POLIDO', 'CHAPA 2MM', 'CROMADO',
                'CROMADO/POLIDO', 'FERRO', 'INOX', 'INOX ESCOVADO', 'INOX POLIDO',
                'METAL', 'METAL CROMADO', 'METAL ESCOVADO', 'METAL POLIDO', 
                'METAL/MADEIRA', 'METAL/PLÁSTICO', 'METÁLICO', 'TUBO 19MM', 
                'TUBO METÁLICO', 'TUBO REDONDO'
            ],
            'MADEIRA': [
                'FAIA', 'FAIA COR NATURAL', 'FAIA NATURAL', 'MADEIRA', 'MDF 45 MM', 'PINHO'
            ],
            'PLASTICO': [
                'FERRO PLÁSTICO', 'PLÁSTICO', 'METAL/PLÁSTICO'
            ],
            'OUTROS': [
                'CONTRAPLACADO', 'SEM INFO', '(EM BRANCO)'
            ]
        }



    def get_data(self):
        all_data = {}

        for n in range(3 ,self.sheet_feets.nrows):
            codigo = self.sheet_feets.cell_value(n, 1)
            altura = self.sheet_feets.cell_value(n, 3)
            material = self.sheet_feets.cell_value(n, 4)
            pdf_file = f'{self.pdf_url}/{codigo}.pdf'
            try:
                data = {
                        'codigo':codigo.split(' ')[1],
                        'altura':self.filter_ints(altura),
                        'material':material.strip().upper(),
                        'pdf_file':pdf_file
                    }
                all_data[codigo.split(' ')[1]] = data
            except IndexError:
                pass
    
        return all_data



    def filter_data(self, code=None, altura=None, material=None):
        all_data = self.get_data()
        filtered_data = []

        for d, option in all_data.items():
            #filter by code -f code
            if code and int(d) == int(code):
                if option not in filtered_data:
                    filtered_data.append(option)
                    break
            #filter by altura -f altura
            if altura and not material:
                if altura and option['altura'] == altura:
                    if option not in filtered_data:
                        filtered_data.append(option)
            #filter by material -f material 
            if material and not altura:
                if option['material'] in self.materials_dict[material.upper()]:
                    if option not in filtered_data:
                        filtered_data.append(option)
            if material and altura:
                if option['material'] in self.materials_dict[material.upper()] and option['altura'] == altura:
                    if option not in filtered_data:
                        filtered_data.append(option)


        return filtered_data


    #helpers
    def filter_ints(self, item):
        item_str = str(item)
        numbers = [int(num) for num in re.findall(r'\d+', item_str)]
        if not numbers: 
            return None
        return self.round_half_up(max(numbers))
    

    def round_half_up(self, num):
        if num % 10 == 5:
            return num
        return round(num, -1)
    


if __name__ == '__main__':

    input_1 = '-c 921'
    input_2 = '-m madeira'
    input_3 = '-a 120'
    input_4 = '-ma madira 40'

    def inputs(promp):
        conn = FEETS()
        if '-c' in promp:
            code = promp.split(' ')[1]
            conn.filter_data(code=code)


    data = FEETS().filter_data(code=952)
    print(f'Total: {len(data)}')
    for d in data:
        print(d['codigo'])