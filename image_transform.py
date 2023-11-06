from io import BytesIO

from PIL import Image


def image_to_matrix(image_bytes: bytes, desired_height: int, desired_width: int) -> list[list[list[list[float]]]]:
    # Load the image from bytes
    img = Image.open(BytesIO(image_bytes))

    # Resize the image to the desired dimensions
    img = img.resize((desired_width, desired_height))

    # Convert image to RGB
    img = img.convert("RGB")

    # Extract RGB values
    r_list, g_list, b_list = [], [], []
    for y in range(desired_height):
        r_row, g_row, b_row = [], [], []
        for x in range(desired_width):
            r, g, b = img.getpixel((x, y))
            r_row.append(r / 255.0)
            g_row.append(g / 255.0)
            b_row.append(b / 255.0)
        r_list.append(r_row)
        g_list.append(g_row)
        b_list.append(b_row)

    return [r_list, g_list, b_list]


if __name__ == '__main__':
    with open('image_example.png', 'rb') as f:
        print(image_to_matrix(f.read(), 32, 32))
