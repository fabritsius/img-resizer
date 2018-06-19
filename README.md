# Image Resizer Python Script

Sometimes you need to resize a lot of images to the same size. There are special tools for developers to do that, but most such projects are larger than they should be. You need to install an app and then learn how to use it.

I decided to solve this issue by coding my own simple solution which does only this one thing (resizing multiple images). There are no bonus features, but you get a very simple usage and an easy installation process.

### Usage

0. Prepare by moving images you want to resize in one folder;
1. Open Terminal and go the directory you have python script saved;
2. Type `python3 img_resizer.py ~/Documents/chosen_images`;
    - try dragging path to the terminal
    - path can be relative to the python file
    - you can set width in the terminal by providing more arguments after path<br>`python3 img_resizer.py ./imgs 144 360 2077`
    - if there is no arguments after path, set width in the script
3. Press _Enter_. New folder will be created with all resized images.

### Installation

0. You need _python3.6_ installed with _Pillow_ library;
1. Obtain the code from _img_resizer.py_. Your choices (one is enough):
     - clone this repo `git clone fabritsius/img-resizer`
     - copy-paste the code manually
     - just curl-it
     - something else
2. Put it somewhere and you are done.