import secrets
import string

def generate_secure_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_characters = letters + digits + punctuation

    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(punctuation),
    ]

    password += [secrets.choice(all_characters) for _ in range(length - 3)]
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

secure_password = generate_secure_password(16)
print("Generated secure password:", secure_password)

