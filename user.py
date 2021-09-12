from skimage import io
import matplotlib.pyplot as plt
from image import apply_preset
from classify import choose_presets

def load_image(path_to_image):
    original_user_image = io.imread(path_to_image)
    return original_user_image

def auto_edit(string_path, desired_style):
    working_image = load_image(string_path)
    presets = choose_presets(desired_style)
    for i in presets.keys():
        working_image = apply_preset(working_image, i, presets[i])
    plt.imshow(working_image)
    plt.show()
    return working_image

def revert_image(string_path):
    return load_image(string_path)

auto_edit("data/0.jpg", "grunge black dark")

