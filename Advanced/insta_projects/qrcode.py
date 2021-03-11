# import qrcode
import pyqrcode
import png
from qrcode import QRCode
s = "www.instagram.com/wazimu.hb/"
# url = qrcode.create(s)
url = pyqrcode.create(s)
url.png('myqr.png', scale = 6)