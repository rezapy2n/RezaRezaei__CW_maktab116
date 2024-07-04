class CredentialsManager:
    def __init__(self):
        self._username = None
        self._password = None

    def set_credentials(self, username, password):
       
        if len(username) >= 5 and len(password) >= 8:
            self._username = username
            self._password = password
        else:
            print("Invalid credentials. Username must be at least 5 characters, and password must be at least 8 characters.")

    def get_username(self):
       
        return self._username

    def get_masked_password(self):
        
        return "*" * len(self._password)


manager = CredentialsManager()
manager.set_credentials("SasyMankan", "TeranTokyo")

print(f"Username: {manager.get_username()}")
print(f"Masked Password: {manager.get_masked_password()}")
