import qrcode

data = "" 

userData = input("Enter some data: ")
print(f"generated qr code with data\n{userData}")

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size (default is 4)
)

qr.add_data(userData)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

output_file = "qrcodeimage_qr.png"
img.save(output_file)

print(f"QR Code generated and saved as '{output_file}'")
