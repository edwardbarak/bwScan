from PIL import Image
import os
import glob

def rotate(path, degrees, save_name):
    im = Image.open(path)
    im.rotate(degrees, expand=1).save(save_name)
    print('Rotated image by ' + str(degrees) + ' degrees and saved as ' + save_name)

def crop(path, x1, y1, x2, y2):
    # crop from (x1, y1) to (x2, y2)
    pass

def black_white_scan(path):
    # turn up contrast
    pass

def binary_search(top, bot):
    median = (top - bot) / 2 + bot
    return median

def rename_imgs_to_nums(path, filetype, start, step=1):
    images = glob.glob(path + '*.' + filetype)
    images.sort()
    cnt = start
    for image in images:
        print('Renaming ' + str(image) + '...')
        os.rename(image, path + str(cnt) + '.' + filetype)
        cnt += step

# useful to combine this with binary search to find missing or extra pages 
def rename_reduce_nums(path, filetype, start, stop, step=1, unary=1 ):
    fnums = range(start, stop, step)
    for fnum in fnums:
        os.rename(path + str(fnum) + '.' + filetype, path + str(fnum + unary) + '.' + filetype)

pwd = os.getcwd()
