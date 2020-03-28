import colorlover as cl

"""
setting up some helper functions that will help us move forward. hex to rgb, rgb to hex. This will help access the colors out of matplotlib if we want them in plotly.
Because of how rgb and hex colors (cmyk & hsl, too probably) work as a simple ecoding I can use my own helper functions to handle the decoding/encoding

in the rgb spectrum a color exists as a 3-tuple of data each within the range 0-255.
* (0, 0 , 0) is black
* (255,255,255) is white 
* this gives 256^3 (16 Million) possible color combinations

hex color behaves similarily but each color is represented in python as a string with the prefix `#`, ie,  `"#FFFFFF"` is equivalent to (255, 255, 255)
Because FF is the equivalent to 255 in base 16 (hex)

There's also an `alpha` property in both, a 4th set of numbers representing transparency but we can leave that alone for now

To convert between the two you simply convert each rgb value to hex, format & return as string
To convert back from hex to rgb, you reverse the process.
"""

def hex_string_to_rgb(h):
    """
    :param h: str '#FFFFFF' to convert from hex to rgb
    :return: rgb tuple
    """ 
    return tuple(int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex_string(r):
    """
    :param r: tuple of valid rgb values
    :return: hex string
    """
    conversion = ''.join([str(hex(_r)).lstrip('0x') for _r in r])
    return f'#{conversion}'


def rgb_to_html_display(name, rgb):
    """
    colorlover cl.to_html returns a div based on the input color
    If we have a name associated, hack the div and give it a title so it has a 
    Hover value in jupyter
    :param name: string name to fill div
    :param rgb: tuple of rgb values
    """
    rgb_as_html = cl.to_html([rgb])
    return '<div title="{}" {}'.format(name, rgb_as_html.split('<div ')[-1])

