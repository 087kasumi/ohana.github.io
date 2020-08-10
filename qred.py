import qrcode

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)

qr.add_data("https://087kasumi.github.io/ohana.github.io/")
qr.make()
img = qr.make_image(fill_color="#23dda0", back_color="red")

img.save("qrcode/087qrcode.png")

