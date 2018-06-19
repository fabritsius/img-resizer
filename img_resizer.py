import os, sys
from PIL import Image

# this is a tuple so ...
# leave one comma when there is a single value
WIDTHS = 250, 400, 800

def resize(in_images_path, WIDTHS):
    out_images_path = in_images_path + '_sized'
    # Create a directory for an OUTPUT
    if not os.path.exists(out_images_path):
        os.makedirs(out_images_path)
    # Tiny error prevention attempt
    if not WIDTHS:
        sys.exit('Add target-WIDTHS in code or as an arguments')
    # User-friendly interface
    print(f'From:\t{in_images_path}')
    print(f'to:\t{out_images_path}')
    # Do for every detected WIDTH
    for w in WIDTHS:
        w = int(w)
        print(f'\nWIDTH {w}')
        for img_name in os.listdir(in_images_path):
            new_name = f"{img_name.split('.')[0]}_{w}w.{img_name.split('.')[-1]}"
            img_path = os.path.join(in_images_path, img_name)
            new_path = os.path.join(out_images_path, new_name)
            try:
                img = Image.open(img_path)
                size = w, int(w/img.size[0]*img.size[1])
                img = img.resize(size, Image.ANTIALIAS)
                img.save(new_path)
                print(new_name)
            except IOError:
                print(f'__ERROR with {new_name}🤭')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Paths calculations
        in_images_path = sys.argv[1]
        # Prefer WIDTHS from terminal arguments
        if len(sys.argv) > 2:
            WIDTHS = sys.argv[2:]
        resize(in_images_path, WIDTHS)
    else:
        sys.exit('Add a path with images in code or as an arguments')

print('\nDone😅')