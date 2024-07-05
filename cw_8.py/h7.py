class EmailAccount:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            print("Invalid email format. Please provide a valid email address.")

    def get_masked_password(self):
        return "*" * len(self.__password)

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            print("Password must be at least 8 characters long.")

    def display_account_info(self):
        print(f"Email: {self.__email}")
        print(f"Masked Password: {self.get_masked_password()}")


my_account = EmailAccount("user@example.com", "securepassword")
my_account.display_account_info()
my_account.set_email("rrezaee74@yahoo.com")
my_account.set_password("wowthewow")
my_account.display_account_info()
