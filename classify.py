key_words = {"blue": [1], "green": [2], "red": [3], 
"yellow" : [8], "pink" : [3, 9], "turquoise" : [1, 2, 10], "contrast" : [4, 7], 
"moody" : [7], "dark" : [4, 6, 7], "bright" : [5, 7], "light" : [4, 5,7], "shadows" : [6, 7], 
"shadow" : [6, 7], "shadowy" : [6, 7], "highlight" : [1, 2, 3, 5, 7], "highlights" : [1, 2, 3, 5, 7], 
"highlighted" : [1, 2, 3, 5, 7], "saturate" : [1, 2, 3, 5, 7], "saturated" : [1, 2, 7], "desaturate" : [8, 9, 10],
"desaturated" : [8, 9, 10], "cool" : [1, 2, 10], "warm": [3, 8], "colorful": [1, 2, 3], "soft": [1, ], "harsh" : [1, 2, 3, ], 
"bold": [1, 7], "vibrant": [1, 2, 3, 7, 8, 9, 10], "black": [4, 6, 7], "white": [4, 5, 7], "dreamy": [1, 5, 8, 9], "grunge": [4, 8], "sunny": [3, 5, 8],
"clean": [7], "hue": [1, 2, 3, 8, 9, 10]}

def choose_presets(user_input):
    words = user_input.split(" ") 
    all_preset_info = []
    unrecognized_words = []
    for word in words:
        try: 
            presets = key_words[word]
            all_preset_info = all_preset_info + presets
        except:
            key_words[word] = []
            unrecognized_words.append(word)
    size = len(all_preset_info)
    preset_counts = {}
    for preset in all_preset_info:
        try:
            preset_counts[preset] = preset_counts[preset] + 1
        except:
             preset_counts[preset] = 1
    presets = {}
    for key in preset_counts.keys():
        presets[key] = preset_counts[key] / size
    return presets
    
