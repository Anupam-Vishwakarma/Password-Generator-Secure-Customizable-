import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a secure random password based on user preferences."""

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type must be selected!")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    print("===  Secure Password Generator ===")

    try:
        length = int(input("Enter password length (e.g., 12): ").strip())
        if length <= 0:
            print(" Length must be greater than 0.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n Your secure password:")
        print(f" {password}")

    except ValueError as e:
        print(" Error:", e)


if __name__ == "__main__":
    main()
