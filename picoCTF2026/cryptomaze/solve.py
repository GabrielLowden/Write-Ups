import codecs
bits = "11011010001000111101000110110010101010010110100100110111101001000010011111001000001011001011100001101010101000101010000010010001"

byte0 = bits[0:8]
byte1 = bits[8:16]
byte2 = bits[16:24]
byte3 = bits[24:32]
byte4 = bits[32:40]
byte5 = bits[40:48]
byte6 = bits[48:56]
byte7 = bits[56:64]
byte8 = bits[64:72]
byte9 = bits[72:80]
byte10 = bits[80:88]
byte11 = bits[88:96]
byte12 = bits[96:104]
byte13 = bits[104:112]
byte14 = bits[112:120]
byte15 = bits[120:128]

byte0 = int(byte0, 2)
byte1 = int(byte1, 2)
byte2 = int(byte2, 2)
byte3 = int(byte3, 2)
byte4 = int(byte4, 2)
byte5 = int(byte5, 2)
byte6 = int(byte6, 2)
byte7 = int(byte7, 2)
byte8 = int(byte8, 2)
byte9 = int(byte9, 2)
byte10 = int(byte10, 2)
byte11 = int(byte11, 2)
byte12 = int(byte12, 2)
byte13 = int(byte13, 2)
byte14 = int(byte14, 2)
byte15 = int(byte15, 2)
key = [hex(byte0), hex(byte1), hex(byte2), hex(byte3), hex(byte4), hex(byte5), hex(byte6), hex(byte7), hex(byte8), hex(byte9), hex(byte10), hex(byte11), hex(byte12), hex(byte13), hex(byte14), hex(byte15)]
for _ in range(16):
    print(key[_], end="")
print()
flag_hex = "8f0e6d0f5b0dc1db201948b9e0cebd8f8c5f092ee437b94b998be7b14dbe7c0b38338e7e04fbddef0c6260a4eb758417"
flag_bytes = bytes.fromhex(flag_hex[2:])
print(flag_bytes)