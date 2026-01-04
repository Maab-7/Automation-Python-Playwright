VALID_USER = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"

INVALID_CASES = [
    ("tomsmith", "badpass", "Your password is invalid!"),
    ("baduser", "SuperSecretPassword!", "Your username is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"),
]
