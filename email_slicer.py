"""
Email Slicer
Splits email into username and domain.
"""
def email_slicer(email):
    username, domain = email.split('@')
    return username, domain

if __name__ == "__main__":
    email = input("Enter your email: ")
    user, dom = email_slicer(email)
    print(f"Username: {user}\nDomain: {dom}")
