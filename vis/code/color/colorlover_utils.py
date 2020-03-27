import colorlover as cl


def hex_string_to_rgb(h):
    """
    returns hex string as rgb tuple
    """ 
    return tuple(int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex_string(r):
    """
    :param r: tuple of valid rgb values
    :return: hex string
    """
    conversion = ''.join([str(hex(_r)).lstrip('0x') for _r in r])
    return f'#{conversion}'