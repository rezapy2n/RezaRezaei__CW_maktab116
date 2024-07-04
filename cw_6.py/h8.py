import re

class Validator:
    @classmethod
    def is_valid_email(cls, email):
      
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))


email_to_check = "rrezaee74@yahoo.com"
if Validator.is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid ")
else:
    print(f"{email_to_check} is not a valid ")
