from datetime import date, timedelta

class DateHelper:
    @classmethod
    def get_next_day(cls, input_date):
 
        return input_date + timedelta(days=1)

my_date = date(2024, 8, 31)
next_day = DateHelper.get_next_day(my_date)
print(f"Next day: {next_day}")
