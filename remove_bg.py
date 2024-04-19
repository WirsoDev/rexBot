#from rembg import remove
#from PIL import Image
#import os

'''
file = './teste.jpg'
out_file = './rm_bg.png'

image = Image.open(file)
output = remove(image, post_process_mask=True)
output.save(out_file)
'''

def remove_bg(path, filetipe='png'):

    #get all images in folder
    print('--- Running remove GB ---')
    print('\n')
    images = os.listdir(path)

    #out folder
    out_folder = path + f'\REM_BG_{filetipe.upper()}'
    if os.path.isdir(out_folder):
        pass
    else:
        os.mkdir(out_folder)

    #filter images (jpg, tiff, png)
    filter_ = ['JPG','JPEG', 'PNG', 'TIFF']
    filtered_images = []
    for i in images:
        try:
            if i.split('.')[1].upper() in filter_:
                filtered_images.append(i)
        except IndexError:
            pass
    print(f'-> Found {len(filtered_images)} in folder')

    print('-> Removing backgroung')
    for imgs in filtered_images:
        print(f'    try image -> {imgs}')
        open_image = Image.open(path + f'\{imgs}')
        remove_bg = remove(open_image, post_process_mask=True, alpha_matting_background_threshold=250, alpha_matting_foreground_threshold=2, alpha_matting_erode_size=2)

        remove_bg.save(out_folder + f"\{imgs.split('.')[0]}" + f'.{filetipe}')
    
    return len(filtered_images)