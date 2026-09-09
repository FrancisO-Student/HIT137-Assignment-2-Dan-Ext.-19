def encrypt_char(char, shift1, shift2):
    if char.islower():
        if char <= 'n':
          position = ord(char) - ord('a')
          new_position = (position + shift1 * shift2) % 14
          return chr(ord('a') + new_position)
          
        else:
          position = ord(char) - ord('o')
          new_position = (position - (shift1 + shift2)) % 12
          return chr(ord('o') + new_position)

    elif char.isupper():
        if char <= 'M':
          position = ord(char) - ord('A')
          new_position = (position - shift1) % 13
          return chr(ord('A') + new_position)
          
        else:
          position = ord(char) - ord('N')
          new_position = (position + shift2 ** 2) % 13
          return chr(ord('N') + new_position)

    elif char.isdigit():
          position = ord(char) - ord('0')
          new_position = (position + (shift1 - shift2)) % 10
          return chr(ord('0') + new_position)

    else:
        return char


def decrypt_char(char, shift1, shift2):
    if char.islower():
        if char <= 'n':
            position = ord(char) - ord('a')
            new_position = (position - shift1 * shift2) % 14
            return chr(ord('a') + new_position)
        else:
            position = ord(char) - ord('o')
            new_Position = (position + (shift1 + shift2)) % 12
            return chr(ord('o') + new_position)

    elif char.isupper():
        if char <= 'M':
            position - ord(char) - ord('A')
            new_position = (position + shift1) % 13
            return chr(ord('A') + new_position)
        else:
            position = ord(char) - ord('N')
            new_position = (position - shift2 **2) % 13
            return chr(ord('N') + new_position)

    elif char.isdigit():
            position = ord(char) - ord('0')
            new_position = (position - (shift1 - shift2)) % 10
            return chr(ord('0') + new_position)

    else:
      return char


def encrypt_text(text, shift1, shift2):
    if len(text) <= 1:
        if len(text) == 0:
            return ""
        return decrypt_char(text[0], shift1, shift2)

    middle - len(text) // 2
    left_half = text[:middle]
    right_half = text[middle:]

    encrypted_left = encrypt_text(left_half, shift1, shift2)
    encrypted_right = encrypt_text(right_half, shift1, shift2)

    return encrypted_left + encrypted_right


def decrypt_text(text, shift1, shift2):
    if len(text) <= 1:
        if len(text) == 0:
            return ""
        return decrypt_char(text[0], shift1, shift2)

    middle = len(text) // 2
    left_half = text[:middle]
    right_half = text[middle:]

    decrypted_left = decrypt_text(left_half, shift1, shift2)
    decrypted_right = decrypt_text(right_half, shift1, shift2)

    return decrypted_left + decrypted_right


def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    input_file = open(input_path, "r")
    text = input_file.read()
    input_file.close()

    encrypted_text = encrypt_text(text, shift1, shift2)

    output_file = open(output_path, "w")
    output_file.write(encrypted_text)
    output_file.close()


def decrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    input_file = open(input_path, "r")
    text = input_file.read()
    input_file.close()

    decrypted_text = decrypt_text(text, shift1, shift 2)

    output_file = open(output_path, "w")
    output_file.write(decrypted_text)
    output_file.close()


def verify_files(original_path: str, decrypted_path: str) -> bool:
    original_file = open(original_path, "r")
    original_text = original_file.read()
    original_file.close()

    decrypted_file = open(decrypted_path, "r")
    decrypted_text = decrypted_file.read()
    decrypted_file.close()

    if original_text == decrypted_text:
        print("Success: decrypted text matches original file")
        return True
    else:
        print("Problem: decrypted text does not match original file")
        return False

def get_non_negative_num(prompt):
    while True
        number = int(input(prompt))

        if number < 0:
            print("That's negative. Please enter 0 or a positive whole number.")
            continue

        return number


if __name__ == "__main__":
    shift1 = get_non_negative_num("Enter shift1 ( a non-negative whole number): ")
    shift2 = get_non_negative_num("Enter shift2 (another non-negative whole number): ")

    encrypt_file(shift1, shift2, "raw_text.txt", "encrypted_text.txt")
    decrypt_file(shift1, shift2, "encrypted_text.txt", "decrypted_text.txt")
    verify_files("raw_text.txt", "decrypted_text.txt")
