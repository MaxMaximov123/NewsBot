from PIL import Image


def image_filter(pixels, i, j, brigh=0, RGB=(0, 0, 0)):
    """Здесь brigh это то, на сколько
       увеличивать яркость пикселя, R - на сколько увеличить красный пигмент, G - на сколько
       увеличить зеленый пигмент, B - на сколько увеличить синий пигмент"""
    r, g, b = pixels[i, j]
    r += brigh + RGB[0]
    g += brigh + RGB[1]
    b += brigh + RGB[2]
    pixels[i, j] = r, g, b
    return pixels[i, j]


print(help())

im1 = Image.open("image/img_1.png")
x, y = im1.size
pixels = im1.load()
for i in range(x):
    for j in range(y):
        pixels[i, j] = image_filter(pixels, i, j, 5, (20, 15, 25))

im1.save("res.jpg")