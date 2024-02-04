import os
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border =3, )

print("Hello, welcome to the QR Code Generator :) ")

print("Please enter your Link/URL to create your QR Code: ")

qr.add_data(input())  # Takes the input as Link for QR code creation.

qr.make(fit=True) # Must have entered the link to able to run which means fit=True.

img = qr.make_image(fill_color="white",back_color="blue")

print("Do you want to customize a logo for your QR Code?")
print("YES? --->  Press 1")
print("NO?  --->  Press 2")
choice = int(input())


if choice==1:


    # Loads the logo image
    print("Enter the path of your logo file:")
    logo_path = input()

    # Check if the file exists
    if os.path.isfile(logo_path):
        # Attempt to open the image file
        try:
            logo_img = Image.open(logo_path)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)

    # Calculate the maximum size for the centered logo
    max_logo_size = min(img.width, img.height) // 2

    # Resize the logo image with a larger factor
    resize_factor = 0.4  # Adjust this value as needed
    new_size = (int(logo_img.width * resize_factor), int(logo_img.height * resize_factor))
    logo_img = logo_img.resize(new_size)

    # Shift the logo towards the right of the center
    shift_factor = 5.2  # Adjust this value to control the shift
    paste_position = ((img.width - logo_img.width) // 2 + int(img.width * shift_factor),
                      (img.height - logo_img.height) // 2)

    # Paste the logo image onto the QR code image at the adjusted position
    img.paste(logo_img, paste_position)

if choice==2 or choice==1:
    print("Enter the file name to save your QR Code:")
    img.save(input()+'.jpg')

    # Get the current working directory
    current_dir = os.getcwd()

    # Print the current working directory
    print("Your QR Code has been generated successfully!")

    print(f"Your QR Code is safely stored, follow this path : \"{current_dir}\"")

else:
    print("Please enter the valid input  :(   ")