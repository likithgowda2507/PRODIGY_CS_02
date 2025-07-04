from PIL import Image

def encrypt_image(input_image, output_image, key):
    image = Image.open(input_image)
    encrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    encrypted_pixels = encrypted_image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            r_enc = (r + key) % 256
            g_enc = (g + key) % 256
            b_enc = (b + key) % 256
            encrypted_pixels[x, y] = (r_enc, g_enc, b_enc)

    encrypted_image.save(output_image)
    print(f"Encrypted image saved as {output_image}")
    print("Displaying input and encrypted image...")
    image.show(title="Original Image")
    encrypted_image.show(title="Encrypted Image")

def decrypt_image(input_image, output_image, key):
    image = Image.open(input_image)
    decrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    decrypted_pixels = decrypted_image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            r_dec = (r - key) % 256
            g_dec = (g - key) % 256
            b_dec = (b - key) % 256
            decrypted_pixels[x, y] = (r_dec, g_dec, b_dec)

    decrypted_image.save(output_image)
    print(f"Decrypted image saved as {output_image}")
    print("Displaying input and decrypted image...")
    image.show(title="Encrypted Image")
    decrypted_image.show(title="Decrypted Image")

def main():
    print("=== Image Pixel Encryption Tool ===")
    while True:
        choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt an image:\n").lower()

        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue

        input_image = input("Enter input image path (e.g., image.png): ").strip('"')
        output_image = input("Enter output image path (e.g., encrypted.png): ").strip('"')


        try:
            key = int(input("Enter encryption key (0-255): "))
            if key < 0 or key > 255:
                raise ValueError
        except ValueError:
            print("Key must be an integer between 0 and 255.")
            continue

        if choice == 'encrypt':
            encrypt_image(input_image, output_image, key)
        else:
            decrypt_image(input_image, output_image, key)

        again = input("Do you want to process another image? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
