# Forensics Bento Challenge Write-Up
+ Author: Gabe Lowden

## Challenge Details
- **Challenge Name**: SUDO MAKE ME A SANDWICH
- **Category**: General Skills
- **Difficulty**: [...]
- **Points**: [50]
- **Author**: [Darkraicg492]
- **Platform**: [picoCTF]

## Challenge Description
Can you read the flag? I think you can!
Additional details will be available after launching your challenge instance.

ssh -p 54040 ctf-player@green-hill.picoctf.net using password 61ecc684

## Solution

- "ls -la", shows that only root has read permissions for flag.txt
- "sudo cat flag.txt", denied access
- "sudo -l", to list commands the user can use
    - given /bin/emacs a text editor
- "sudo emacs flag.txt", to view flag

## Flag(s)

picoCTF{ju57_5ud0_17_4c6f730f}

## Other Thoughts

## References

---