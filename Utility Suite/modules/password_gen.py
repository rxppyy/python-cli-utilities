import secrets

def generatePassword(pass_length):
    password = secrets.token_urlsafe(pass_length)[:pass_length]
    return password