from PIL import Image
import os

def encrypt_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Convert the image to RGB mode
    img = img.convert("RGB")
    # Encrypt the image by swapping red and blue channels
    encrypted_img = img.copy()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            encrypted_img.putpixel((x, y), (b, g, r))
    # Determine the directory of the original image
    directory = os.path.dirname(image_path)
    # Save the encrypted image in the same directory
    encrypted_img.save(os.path.join(directory, "encrypted_image.png"))
    return encrypted_img

def decrypt_image(encrypted_image_path):
    # Open the encrypted image file
    encrypted_img = Image.open(encrypted_image_path)
    # Convert the image to RGB mode
    encrypted_img = encrypted_img.convert("RGB")
    # Decrypt the image by swapping red and blue channels back
    decrypted_img = encrypted_img.copy()
    for x in range(encrypted_img.width):
        for y in range(encrypted_img.height):
            r, g, b = encrypted_img.getpixel((x, y))
            decrypted_img.putpixel((x, y), (b, g, r))
    # Determine the directory of the encrypted image
    directory = os.path.dirname(encrypted_image_path)
    # Save the decrypted image in the same directory
    decrypted_img.save(os.path.join(directory, "decrypted_image.png"))
    return decrypted_img

if __name__ == "__main__":
    # Path to the original image
    original_image_path = "TASK2\img.jpg"

    # Encrypt the image
    encrypted_image = encrypt_image(original_image_path)
    print("Image encrypted successfully.")

    # Decrypt the image
    decrypted_image = decrypt_image(os.path.join(os.path.dirname(original_image_path), "encrypted_image.png"))
    print("Image decrypted successfully.")
