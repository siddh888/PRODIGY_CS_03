import re


def assess_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. Minimum length should be 8 characters.")
    elif len(password) <= 12:
        score += 1
        feedback.append("Password length is moderate. Consider making it longer.")
    else:
        score += 2
        feedback.append("Password length is good.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback.append(f"Overall password strength: {strength}")

    return feedback

password = input("Enter a password to assess: ")
feedback = assess_password_strength(password)

for comment in feedback:
    print(comment)
