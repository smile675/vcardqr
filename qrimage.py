import qrcode
from PIL import Image
from qrcode.image.svg import SvgImage

class QrImage:
    def __init__(self, vcard_string, filename="vcard", output_format="png", fill="black", background="white"):
        self.vcard_string = vcard_string
        self.filename = filename
        self.output_format = output_format.lower()
        self.fill = fill
        self.background = background

    def generate(self):
        if self.output_format == "svg":
            factory = SvgImage
        else:
            factory = None

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(self.vcard_string)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fill, back_color=self.background, image_factory=factory)

        output_file = f"{self.filename}.{self.output_format}"

        if self.output_format == "jpg":
            img = img.convert("RGB")  # Convert to RGB for JPG
        img.save(output_file)

        print(f"QR code saved as {output_file}")

