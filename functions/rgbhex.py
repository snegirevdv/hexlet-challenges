# https://ru.hexlet.io/challenges/python_functions_rgb_hex_conversion_exercise


def rgb2hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def hex2rgb(hexcode: str) -> dict[str, int]:
    return dict(
        r=int(hexcode[1:3], 16),
        g=int(hexcode[3:5], 16),
        b=int(hexcode[5:], 16)
    )
