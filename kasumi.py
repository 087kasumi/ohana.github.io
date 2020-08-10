import qrcode

img = qrcode.make("https://087kasumi.githud.io/ohana.github.io/")

print(type(img))
print(img.size)
img.save("qrcode/087qrcode.png")
