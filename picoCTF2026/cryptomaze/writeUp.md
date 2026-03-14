# Write-Up
+ Author: Gabe Lowden

## Challenge Details
- **Challenge Name**: cryptomaze
- **Category**: Cryptography
- **Difficulty**: []
- **Points**: [100]
- **Author**: [Sabine Gisagara]
- **Platform**: [picoCTF]

## Challenge Description
In this challenge, you are tasked with recovering a hidden flag that has been encrypted using a combination of Linear Feedback Shift Register (LFSR) and AES encryption. The LFSR is used to derive a key for AES encryption, making it crucial to understand its workings to decrypt the message.
The flag has been stored in a file and encrypted. Your goal is to derive the key used for encryption from the LFSR state and taps provided in the output, and then decrypt the flag to retrieve it.
Download the encrypted flag from here. which contains the following information:
- The initial state of the LFSR
- The taps used for the LFSR
- The encrypted flag in hexadecimal format

## Files Provided
- output.txt     

## Solution
- use lsfr init state and taps to gen. a 128-bit seq.
    - [11011010001000111101000110110010101010010110100100110111101001000010011111001000001011001011100001101010101000101010000010010001]
- convert 128-bit seq. into 16-byte AES key by: group bits into 8-bit chunks, conv. each chunk from binary to byte to form aes key
-
## Flag(s)

## Other Thoughts

## References

---