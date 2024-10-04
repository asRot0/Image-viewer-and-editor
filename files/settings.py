from pathlib import Path

# Assuming the script is in the "files" directory, want to move two levels up
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves two levels up to project root

# Define the assets path
assets_dir = BASE_DIR / 'assets'


# Define the paths relative to the assets directory
title_ico = assets_dir / 'image.ico'
left_image = os.path.join(BASE_DIR, '../assets/left.png')
left_enter_image = os.path.join(BASE_DIR, '../assets/left-arrow.png')
right_image = os.path.join(BASE_DIR, '../assets/right.png')
right_enter_image = os.path.join(BASE_DIR, '../assets/right-arrow.png')
close_dark = os.path.join(BASE_DIR, '../assets/close.png')
close_image = os.path.join(BASE_DIR, '../assets/x.png')
close_enter_image = os.path.join(BASE_DIR, '../assets/cross.png')
folder_image = os.path.join(BASE_DIR, '../assets/folder.png')
folder_enter_image = os.path.join(BASE_DIR, '../assets/folder1.png')
editing_image = os.path.join(BASE_DIR, '../assets/image-editing.png')
editing_enter_image = os.path.join(BASE_DIR, '../assets/image-editing1.png')
rotate_image = os.path.join(BASE_DIR, '../assets/rotation.png')
rotate_enter_image = os.path.join(BASE_DIR, '../assets/rotation1.png')
wallpaper_image = os.path.join(BASE_DIR, '../assets/wallpaper.png')
wallpaper_enter_image = os.path.join(BASE_DIR, '../assets/wallpaper1.png')
info_image = os.path.join(BASE_DIR, '../assets/info.png')
info_enter_image = os.path.join(BASE_DIR, '../assets/info1.png')
dots_image = os.path.join(BASE_DIR, '../assets/dots.png')
dots_enter_image = os.path.join(BASE_DIR, '../assets/dots1.png')
dinosaur_image = os.path.join(BASE_DIR, '../assets/dinosaur.png')


# values
ROTATE_DEFAULT = 0
ZOOM_DEFAULT = 0
FLIP_OPTIONS = ['None', 'X', 'Y', 'Both']
BLUR_DEFAULT = 0
CONTRAST_DEFAULT = 0
EFFECT_OPTIONS = ['None', 'Emboss', 'Find edges', 'Contour', 'Edge enhance']
BRIGHTNESS_DEFAULT = 1
VIBRANCE_DEFAULT = 1
GRAYSCALE_DEFAULT = False
INVERT_DEFAULT = False

# colors
BACKGROUND_COLOR = '#242424'
WHITE = '#FFF'
GREY = 'grey'
ALERT = '#752d28'
BLUE = '#aec2d1'
BLUE_HOVER = '#d3e1eb'
BLUE_BG = '#90a399'
DARK_GRAY = '#4a4a4a'
CLOSE_RED = '#8a0606'
SLIDER_BG = '#64686b'
SLIDER_BUTTON = '#807e7e'
MENU_BG = '#3e3e40'
BUTTON_BG = '#424242'
BUTTON_BG_HOVER = '#5c5c5c'
BUTTON_COLOR = '#4a4a57'
BUTTON_HOVER_COLOR = '#69697d'
DROPDOWN_MAIN_COLOR = '#444'
DROPDOWN_HOVER_COLOR = '#333'
DROPDOWN_MENU_COLOR = '#666'

# image info
image_info = {
    'image_path': '',
    'image_size': ''

}

# about
about = {
    'title': 'PhotoFly',
    'developer': 'Asif Ahmed (asRot0)',
    'version': '1.0.1',
    'released': '2030',
    'license': 'MIT license',
    'copyright': '© 2024 asRot0'

}