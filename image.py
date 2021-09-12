import numpy as np

def preset_0(image_copy, scale):
    return image_copy

def preset_1(image_copy, scale):
    usable_scale = ((1 - scale) * 3) + 0.8
    left_to_increase = 255 - image_copy[:, :, 2]
    blueness = (image_copy[:, :, 2] / 255)**usable_scale
    blue_to_add = np.multiply(left_to_increase, blueness)
    image_copy[:, :, 2] =  image_copy[:, :, 2] + blue_to_add
    return image_copy

def preset_2(image_copy, scale):
    usable_scale = ((1 - scale) * 3) + 0.8
    left_to_increase = 255 - image_copy[:, :, 1]
    greenness = (image_copy[:, :, 1] / 255)**usable_scale
    green_to_add = np.multiply(left_to_increase, greenness)
    image_copy[:, :, 1] =  image_copy[:, :, 1] + green_to_add
    return image_copy

def preset_3(image_copy, scale):
    usable_scale = ((1 - scale) * 3) + 0.8
    left_to_increase = 255 - image_copy[:, :, 0]
    redness = (image_copy[:, :, 0] / 255)**usable_scale
    red_to_add = np.multiply(left_to_increase, redness)
    image_copy[:, :, 0] =  image_copy[:, :, 0] + red_to_add
    return image_copy

def preset_4(image_copy, scale):
    darks = image_copy < ((255 / 2) * scale)
    image_copy[darks] = image_copy[darks] * (1 - scale)
    lights = image_copy > 255 - ((255 / 2) * scale)
    image_copy[lights] = image_copy[lights] + ((255 - image_copy[lights]) * (1 - scale))
    return image_copy

def preset_5(image_copy, scale):
    usable_scale = scale * 0.5
    red =  255 - image_copy[:, :, 0]
    green = 255 - image_copy[:, :, 1]
    blue = 255 - image_copy[:, :, 2]
    image_copy[:, :, 0] = image_copy[:, :, 0] + (red * usable_scale)
    image_copy[:, :, 1] = image_copy[:, :, 1] + (green * usable_scale)
    image_copy[:, :, 2] = image_copy[:, :, 2] + (blue * usable_scale)
    return image_copy

def preset_6(image_copy, scale):
    usable_scale = scale * 0.5
    red =  image_copy[:, :, 0]
    green = image_copy[:, :, 1]
    blue = image_copy[:, :, 2]
    image_copy[:, :, 0] = image_copy[:, :, 0] - (red * usable_scale)
    image_copy[:, :, 1] = image_copy[:, :, 1] - (green * usable_scale)
    image_copy[:, :, 2] = image_copy[:, :, 2] - (blue * usable_scale)
    return image_copy

def preset_7(image_copy, scale):
    usable_scale = scale * 100
    red_to_white =  image_copy[:, :, 0] > 255 - usable_scale
    green_to_white = image_copy[:, :, 1] > 255 - usable_scale
    blue_to_white = image_copy[:, :, 2] > 255 - usable_scale
    image_copy[:, :, 0][np.logical_or(np.logical_or(
        np.logical_and(red_to_white, green_to_white),
        np.logical_and(red_to_white, blue_to_white)), 
        np.logical_and(green_to_white, blue_to_white))] = 255
    image_copy[:, :, 1][np.logical_or(np.logical_or(
        np.logical_and(red_to_white, green_to_white),
        np.logical_and(red_to_white, blue_to_white)), 
        np.logical_and(green_to_white, blue_to_white))] = 255
    image_copy[:, :, 2][np.logical_or(np.logical_or(
        np.logical_and(red_to_white, green_to_white),
        np.logical_and(red_to_white, blue_to_white)), 
        np.logical_and(green_to_white, blue_to_white))] = 255

    red_to_black =  image_copy[:, :, 0] < usable_scale
    green_to_black = image_copy[:, :, 1] < usable_scale
    blue_to_black = image_copy[:, :, 2] < usable_scale
    image_copy[:, :, 0][np.logical_or(np.logical_or(
        np.logical_and(red_to_black, green_to_black),
        np.logical_and(red_to_black, blue_to_black)), 
        np.logical_and(green_to_black, blue_to_black))] = 0
    image_copy[:, :, 1][np.logical_or(np.logical_or(
        np.logical_and(red_to_black, green_to_black),
        np.logical_and(red_to_black, blue_to_black)), 
        np.logical_and(green_to_black, blue_to_black))] = 0
    image_copy[:, :, 2][np.logical_or(np.logical_or(
        np.logical_and(red_to_black, green_to_black),
        np.logical_and(red_to_black, blue_to_black)), 
        np.logical_and(green_to_black, blue_to_black))] = 0
    return image_copy

def preset_8(image_copy, scale):
    usable_scale = scale * 0.7 
    left_to_decrease = image_copy[:, :, 2] * usable_scale
    blueness = (image_copy[:, :, 2] / 255)
    blue_to_decrease = np.multiply(left_to_decrease, blueness)
    image_copy[:, :, 2] =  image_copy[:, :, 2] - blue_to_decrease
    return image_copy

def preset_9(image_copy, scale):
    usable_scale = scale * 0.7 
    left_to_decrease = image_copy[:, :, 1] * usable_scale
    greenness = (image_copy[:, :, 1] / 255)
    green_to_decrease = np.multiply(left_to_decrease, greenness)
    image_copy[:, :, 1] =  image_copy[:, :, 2] - green_to_decrease
    return image_copy

def preset_10(image_copy, scale):
    usable_scale = scale * 0.7 
    left_to_decrease = image_copy[:, :, 0] * usable_scale
    greenness = (image_copy[:, :, 0] / 255)
    green_to_decrease = np.multiply(left_to_decrease, greenness)
    image_copy[:, :, 0] =  image_copy[:, :, 0] - green_to_decrease
    return image_copy


presets = {
    0: preset_0,
    1: preset_1,
    2: preset_2,
    3: preset_3,
    4: preset_4,
    5: preset_5,
    6: preset_6,
    7: preset_7,
    8: preset_8,
    9: preset_9,
    10: preset_10,
 }

def apply_preset(image, preset, scale):
    if preset == 0:
        new_image = image.copy()
    else:
        image_copy = image.copy()
        new_image = presets[preset](image_copy, scale)
    return new_image
