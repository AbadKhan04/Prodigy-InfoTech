def caesar_encrypt(text, shift):
  encrypted_text = ""
  for char in text:
      if char.isalpha():
          shifted = ord(char) + shift
          if char.islower():
              if shifted > ord('z'):
                  shifted -= 26
              encrypted_text += chr(shifted)
          elif char.isupper():
              if shifted > ord('Z'):
                  shifted -= 26
              encrypted_text += chr(shifted)
      else:
          encrypted_text += char
  return encrypted_text

def caesar_decrypt(text, shift):
  decrypted_text = ""
  for char in text:
      if char.isalpha():
          shifted = ord(char) - shift
          if char.islower():
              if shifted < ord('a'):
                  shifted += 26
              decrypted_text += chr(shifted)
          elif char.isupper():
              if shifted < ord('A'):
                  shifted += 26
              decrypted_text += chr(shifted)
      else:
          decrypted_text += char
  return decrypted_text

def brute_force_decrypt(text):
  for shift in range(1, 10):
      decrypted_text = caesar_decrypt(text, shift)
      print(f"With shift value {shift}: {decrypted_text}")

def main():
  while True:
      print("1) Encryption")
      print("2) Decryption")
      print("3) Exit")
      choice = input("Enter your choice: ")

      if choice == '1':
          text = input("Enter the text to encrypt: ")
          shift = int(input("Enter the shift value: "))
          encrypted_text = caesar_encrypt(text, shift)
          print("Encrypted text:", encrypted_text)
      elif choice == '2':
          decryption_choice = input("Choose decryption method:\n a) Shift value\n b) Brute force (1 - 9)\n")
          text = input("Enter the text to decrypt: ")
          if decryption_choice == 'a':
              shift = int(input("Enter the shift value: "))
              decrypted_text = caesar_decrypt(text, shift)
              print("Decrypted text:", decrypted_text)
          elif decryption_choice == 'b':
              brute_force_decrypt(text)
      elif choice == '3':
          print("Exiting program.")
          break
      else:
          print("Invalid choice. Please choose again.")

if __name__ == "__main__":
  main()
