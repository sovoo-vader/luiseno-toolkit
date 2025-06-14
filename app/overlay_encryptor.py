# OverlayEncryptor – Hide Messages Using Basket-Weaving Logic (visible/invisible strand model)

import random

# Simulate binary overlay using weave pattern (0 = base, 1 = overlay strand)
def weave_encrypt(message):
    binary = ''.join(f'{ord(c):08b}' for c in message)
    overlay_pattern = [('x' if b == '1' else '-') for b in binary]
    lines = [''.join(overlay_pattern[i:i+8]) for i in range(0, len(overlay_pattern), 8)]
    return lines

# Decrypt overlay pattern back to text
def weave_decrypt(overlay_lines):
    binary = ''.join(['1' if c == 'x' else '0' for line in overlay_lines for c in line])
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

# Example use
if __name__ == '__main__':
    secret = "sacred"
    encrypted = weave_encrypt(secret)
    print("Encrypted Pattern:")
    for line in encrypted:
        print(line)

    decrypted = weave_decrypt(encrypted)
    print("\nDecrypted Message:", decrypted)
