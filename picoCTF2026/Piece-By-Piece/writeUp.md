# Write-Up
+ Author: Gabe Lowden

## Challenge Details
- **Challenge Name**: Piece By Piece
- **Category**: General Skills
- **Difficulty**: []
- **Points**: [50]
- **Author**: [Yahaya Meddy]
- **Platform**: [picoCTF]

## Challenge Description
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.
Additional details will be available after launching your challenge instance.

SSH to dolphin-cove.picoctf.net:57248 and login as ctf-player with password 1ad5be0d.

## Solution

- "ls", reveals 6 files, instructions.txt & part_aa...part_ae
    - The instructions tell us the flag is a zip file split into 5 parts & is password protected (pswd in instructions)
- "cat part_aa > combined.zip"
- "cat part_ab >> combined.zip" ...repeat for all parts
- "unzip -x combined.zip
- "cat flag.txt"

## Flag(s)

picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_5b6e506b}

## Other Thoughts

## References

---