from PIL import Image



im = Image.open("fleur.jpg")
print(im.format, im.size, im.mode)

# im.show()

im = im.convert("L")
print(im.format, im.size, im.mode)

im.show()
im.save("fleur_gris.jpg")
im.close()
