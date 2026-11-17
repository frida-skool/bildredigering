from PIL import Image, ImageEnhance, ImageOps

cat = Image.open("images.png")

# Steg 1: Gör svartvit
bw_cat = cat.convert("L")

# Steg 2: Höj kontrasten
hc_cat = ImageEnhance.Contrast(bw_cat).enhance(1.4)

# Steg 3: Minska ljusheten (brightness)
emo_cat = ImageEnhance.Brightness(hc_cat).enhance(0.6)

# Steg 4: Spara bilden
emo_cat.save("emo_cat.png")

with Image.open('images.png') as img:
    # Inverterar alla pixlar över ett visst gränsvärde
    img = ImageOps.solarize(img, 60)

    # Lägger till en ram runt bilder
    img = ImageOps.expand(img, 10, (0, 255, 255))

    # Reducerar bitdjupet (antal färger)
    img = ImageOps.posterize(img, 5)

    # Skalar om en bild
    img = ImageOps.scale(img, 1.2)

    # Vänder en bild upp- och ned
    img = ImageOps.flip(img)

    # Spegelvänder en bild
    img = ImageOps.mirror(img)

    img.save('img_newimage.png')