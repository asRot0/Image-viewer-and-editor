from pathlib import Path

# Assuming the script is in the "files" directory, want to move two levels up
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves two levels up to project root

# Define the assets path
assets_dir = BASE_DIR / 'assets'


# Define the paths relative to the assets directory
title_ico = assets_dir / 'image.ico'
title_png = assets_dir / 'image.png'
left_image = assets_dir / 'left.png'
left_enter_image = assets_dir / 'left-arrow.png'
right_image = assets_dir / 'right.png'
right_enter_image = assets_dir / 'right-arrow.png'
close_dark = assets_dir / 'close.png'
close_image = assets_dir / 'x.png'
close_enter_image = assets_dir / 'cross.png'
folder_image = assets_dir / 'folder.png'
folder_enter_image = assets_dir / 'folder1.png'
editing_image = assets_dir / 'image-editing.png'
editing_enter_image = assets_dir / 'image-editing1.png'
rotate_image = assets_dir / 'rotation.png'
rotate_enter_image = assets_dir / 'rotation1.png'
wallpaper_image = assets_dir / 'wallpaper.png'
wallpaper_enter_image = assets_dir / 'wallpaper1.png'
info_image = assets_dir / 'info.png'
info_enter_image = assets_dir / 'info1.png'
dots_image = assets_dir / 'dots.png'
dots_enter_image = assets_dir / 'dots1.png'
dinosaur_image = assets_dir / 'dinosaur.png'


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
