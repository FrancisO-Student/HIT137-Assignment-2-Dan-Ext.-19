def encrypt_char(char, shift1, shift2):
    if char.islower()
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
