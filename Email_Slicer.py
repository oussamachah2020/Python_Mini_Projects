email = input('Enter your email address: ').strip()

username = email[: email.index('@')]
domain = email[email.index('@') + 1:]

print(f"your username is ({username}) and the domain is ({domain})")