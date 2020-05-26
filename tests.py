from PIL import Image
import os


def resize_img(path, size):

    path.replace('\\', '/')

    files = os.listdir(path)
    if os.path.isdir(path + '/resized_to_' + str(size) + 'px'):
        pass
    else:
        os.mkdir(path + '/resized_to_' + str(size) + 'px')

    count = 0
    for x in files:
        dir_img = path + '/' + files[count]
        img = Image.open(dir_img)
        new_size_y = int(size / (img.size[0] / img.size[1]))
        rezized = img.resize((size, new_size_y))
        save_file = path + '/resized_to_' + str(size) + 'px/' + files[count]
        rezized.save(save_file)
        print(f'image {files[count]} resized!')
        count += 1
        

        

if __name__ == "__main__":
    path = input(': ')
    resize_img(path, 200)