import base64

# Base64 encoded string (ensure padding is correct)
encoded_str = """
aQBmACgAWwBJAG4AdABQAHQAcgBdADoAOgBTAGkAegBlACAALQBlAHEAIAA0ACkAewAkAGIAPQAnAHAAbwB3AGUAcgBzAGgAZQBsAGwALgBlAHgAZQAnAH0AZQBsAHMAZQB7ACQAYgA9ACQAZQBuAHYAOgB3AGkAbgBkAGkAcgArACcAXABzAHkAcwB3AG8AdwA2ADQAXABXAGkAbgBkAG8AdwBzAFAAbwB3AGUAcgBTAGgAZQBsAGwAXAB2ADEALgAwAFwAcABvAHcAZQ...
"""

# Fix the padding issue by adding `=` characters
encoded_str = encoded_str.strip()  # Remove any extra spaces or newlines
padding = len(encoded_str) % 4
if padding != 0:
    encoded_str += '=' * (4 - padding)

# Decode the base64 string
decoded_bytes = base64.b64decode(encoded_str)

try:
    # Try decoding it as UTF-8
    decoded_str = decoded_bytes.decode('utf-8', errors='ignore')  # Ignore errors if there are non-UTF characters
    print(decoded_str)
except UnicodeDecodeError:
    print("The data might not be text or is in a different encoding.")
    # Optional: Save the binary data to a file if it's not textual
    with open("decoded_output.bin", "wb") as f:
        f.write(decoded_bytes)
    print("Binary data saved to decoded_output.bin")