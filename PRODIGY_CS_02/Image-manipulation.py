from PIL import Image


def encrypt_image(image_path, key):
  img = Image.open(image_path)
  width, height = img.size

  encrypted_img = Image.new(img.mode, (width, height))

  for x in range(width):
    for y in range(height):
      pixel = img.getpixel((x, y))
      r, g, b = pixel
      r_encrypted = (r + key) % 256
      g_encrypted = (g + key) % 256
      b_encrypted = (b + key) % 256
      encrypted_img.putpixel((x, y), (r_encrypted, g_encrypted, b_encrypted))

  return encrypted_img


def main():
  image_path = "example_image.jpg"
  key = 50
  encrypted_img = encrypt_image(image_path, key)
  encrypted_img.save("encrypted_image.jpg")
  print("Image encrypted and saved successfully.")


if __name__ == "__main__":
  main()
