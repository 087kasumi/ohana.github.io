import qrcode
import os

file_name = "qrcode/087qrcode_l.png"

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)

qr.add_data("https://087kasumi.github.io/ohana.github.io/")
qr.make()
img = qr.make_image(fill_color="blue", back_color="red")

img.save(file_name)
current_dir = os.getcwd()
print("「{0}\\{1}」にQRコード画像を保存しました".format(current_dir,file_name))
