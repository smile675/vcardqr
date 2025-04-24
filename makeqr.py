from vcard import VCard
from utils import configure_qr
from qrimage import QrImage

def main():
    print("Program running...\n")

    # Load single vCard from CSV
    vcards = VCard.from_csv("data.csv")
    
    if vcards:
        vcard = vcards[0]
        vcard_string = vcard.to_vcard()
        
        style = configure_qr()

        qr = QrImage(
            vcard_string,
            filename="vcard",
            output_format=style["format"],
            fill=style["fill"],
            background=style["background"]
        )
        qr.generate()

    else:
        print("No data found in data.csv.")

if __name__ == "__main__":
    main()
