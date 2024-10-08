import random
import datetime
import string
from db.database import aquinosusers
import xlrd
import os
from PIL import Image, ImageCms
import io


# datetime functions

def weeknum():

    '''returns the number of the current week'''

    date = datetime.date.today().isocalendar()[1]
    return date

def weekday():

    return datetime.datetime.today().weekday()


def find_weeknum(year, mon, day):
    '''
    :param year: Year
    :param mon: Month
    :param day: day
    :return: The function returns a number of a week by the given date
    '''
    date = datetime.date(int(year), int(mon), int(day)).isocalendar()[1]
    return date


# main app's

def resize_img(path, size):


    files_exten = [
        'jpg',
        'JPG',
        'JPEG',
        'png',
        'tiff',
        'tif',
        'TIFF',
        'PNG',
    ]

    print(f'Path to search: {path}')

    files = []
    for file in os.listdir(path):
        x = file.split('.')
        if len(x) > 1:
            if x[1] in files_exten:
                files.append(file)

    extentions = []

    for ext in files:
        if '.' in ext:
            extention = ext.split('.')
            extentions.append(extention[1])

    print(f'{len(extentions)} find!')

    if os.path.isdir(path + '/resized_to_' + str(size) + 'px'):
        pass
    else:
        os.mkdir(path + '/resized_to_' + str(size) + 'px')

    
    count = 0
    for x in files:

        if extentions[count] in files_exten:
            dir_img = path + '/' + files[count]
            img = Image.open(dir_img)

            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            icc = img.info.get('icc_profile', '')

            if icc:
                handler = io.BytesIO(icc)
                src_profile = ImageCms.ImageCmsProfile(handler)
                dst_profile = ImageCms.createProfile('sRGB')

                img = ImageCms.profileToProfile(img, src_profile, dst_profile)

            new_size_y = int(size) / (int(img.size[0]) / int(img.size[1]))
            rezized = img.resize((size, int(new_size_y)), Image.LANCZOS)
            new_name = files[count].split('.')
            save_file = path + '/resized_to_' + str(size) + 'px/' + str(new_name[0]) + '.jpeg'
            rezized.save(save_file, 'JPEG', quality=90)
            print(f'image {files[count]} resized!')
            count += 1
        
        else:
            print(f'{x} not rezized')
            count += 1

    return count
        




def aqpassgen(ctx, givenname=''):

    def findname():
        # extract name by user
        if givenname == '':
            nickname = ctx.author.name
            if nickname == 'Wirso':
                name = 'wilson'
            elif nickname == 'Mrs. Jenni':
                name = 'Jennifer'
            elif nickname == 'dani_a_ventura':
                name = 'Daniela'
            elif nickname == 'Sandro':
                name = 'Sandro'
        else:
            name = ctx.author.name
        return name

    # string list all caracters - no cars on name
    name = findname()
    listchar01 = []
    for itens in string.ascii_uppercase + string.ascii_lowercase:
        if itens not in name.upper() and name.lower():
            listchar01.append(''.join(itens))
    listdig =[str(x) for x in string.digits]
    listnalpha = ['!', '#', '$', '&', '/', '*']

    # ramdom all strings

    r_listchar01 = random.sample(listchar01, k=6)
    r_listdig = random.sample(listdig, k=2)
    r_listnalpha = random.sample(listnalpha, k=2)
    passgen = r_listchar01 + r_listdig + r_listnalpha
    random.shuffle(passgen)
    return ''.join(passgen)



class Dict_tecidos:

    def __init__(self, rev):

        tecidos = (r'EXCEL LIBS/TC_02.xlsx')
        self.sheet_tecidos = xlrd.open_workbook(tecidos).sheet_by_index(0)
        self.rev = rev.strip().upper()

        old_tecidos = (r'EXCEL LIBS/tc_oldlist.xlsx')
        self.sheet_old_tecidos = xlrd.open_workbook(old_tecidos).sheet_by_index(0)


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
            preço = self.sheet_tecidos.cell_value(n, 12)
            dic_preço[codigo] = (preço)

        return dic_preço[self.rev]


    def metros(self):

        dic_metros = {}

        for n in range(self.sheet_tecidos.nrows):
            codigo = self.sheet_tecidos.cell_value(n, 2)
            metros = self.sheet_tecidos.cell_value(n, 5)
            dic_metros[codigo] = (metros)

        return dic_metros[self.rev]

    
    def codigo(self):
        dic_codigo = {}

        for n in range(self.sheet_tecidos.nrows):
            codigo = self.sheet_tecidos.cell_value(n, 2)
            dic_codigo[codigo] = (codigo)

        return dic_codigo[self.rev]

    def gamas(self):

        lista_01 = []
        Lista_02 = []
        parsed_ = ''

        for n in range(self.sheet_tecidos.nrows):
            descrição = self.sheet_tecidos.cell_value(n, 3)
            codigo = self.sheet_tecidos.cell_value(n, 2)
            if self.rev in descrição:
                lista_01.append(f'{descrição} - {codigo}')
        
        for n in range(self.sheet_old_tecidos.nrows):
            descrição = self.sheet_old_tecidos.cell_value(n, 1)
            codigo = self.sheet_old_tecidos.cell_value(n, 2)
            if self.rev in descrição:
                Lista_02.append(f'{descrição} - {codigo}')

        #create set
        set_ = list(set(lista_01 + Lista_02))
        for i in set_:
            parsed_ = parsed_ + f'{i}\n'

        return [parsed_, len(set_)]


        
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


def rexgifs():

    '''Returns random gifs for when rex go's online'''

    frases = ['https://tenor.com/view/dinosaur-trex-summersault-boom-running-gif-9694162',
            'https://tenor.com/view/trex-horse-soccer-what-the-heck-wtf-gif-5080299',
            'https://tenor.com/view/rex-snow-snow-shovel-gif-15013849','https://tenor.com/view/trex-arms-gif-7622211']

    return(random.choice(frases))



def facts():

    file = open('docs/facts.txt', mode='r', encoding='utf-8')

    facts = file.read()
    fact_list = facts.split('\n')

    return random.choice(fact_list)



if __name__ == "__main__":
    pass
