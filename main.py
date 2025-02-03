#!/bin/python

from PIL import Image

# converte um pixel para grayscale
def px_to_grayscale(img, x, y):
  px = img.getpixel((x, y))
  return int((px[0]+px[1]+px[2])/3)

# converte a imagem para grayscale
def img_to_grayscale(img):
  for x in range(img.width):
    for y in range(img.height):
      pxvalue = px_to_grayscale(img, x, y)
      img.putpixel((x, y), (pxvalue, pxvalue, pxvalue))


# converte um pixel para binarizada
def px_to_bin(img, x, y):
  px = img.getpixel((x, y))
  px = int((px[0]+px[1]+px[2])/3)
  return 0  if px < 128 else 255


# converte imagem para binarizada
def img_to_bin(img):
  for x in range(img.width):
    for y in range(img.height):
      pxvalue = px_to_bin(img, x, y)
      img.putpixel((x, y), (pxvalue, pxvalue, pxvalue))



img_path = "chicken.jpg"

img  = Image.open(img_path)

img_to_grayscale(img)
img.save("grayscale.jpg")

img_to_bin(img)
img.save("bin.jpg")


