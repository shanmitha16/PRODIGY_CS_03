import re

def is_minimum_length(password, length=8):
    return len(password) >= length

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_chars.search(password) is not None

def is_complex(password):
    checks = [is_minimum_length(password),
              has_uppercase(password),
              has_lowercase(password),
              has_digit(password),
              has_special_char(password)]
    return all(checks)

def password_feedback(password):
    feedback = []
    if not is_minimum_length(password):
        feedback.append("Password should be at least 8 characters long.")
    if not has_uppercase(password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not has_lowercase(password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not has_digit(password):
        feedback.append("Password should contain at least one digit.")
    if not has_special_char(password):
        feedback.append("Password should contain at least one special character.")
    return feedback

def main():
    password = input("Enter your password: ")
    if is_complex(password):
        print("Password is complex.")
    else:
        print("Password is not complex. Please make sure it meets the complexity criteria.")
        print("Feedback:")
        for point in password_feedback(password):
            print("-", point)

if __name__ == "__main__":
    main()
