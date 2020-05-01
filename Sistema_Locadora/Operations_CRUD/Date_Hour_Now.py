from datetime import datetime


class DateHourNow:

    @staticmethod
    def get_date_hour_now():

        todays_date = datetime.now()
        return todays_date

    @staticmethod
    def get_just_date():
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        if day in(1, 2, 3, 4, 5, 6, 7, 8, 9):
            today = "0{0}/{1}/{2}".format(str(day), str(month), str(year))
            return today
        else:
            today = "0{0}/{1}/{2}".format(str(day), str(month), str(year))
            return today


"""data = DateHourNow()
# data.get_date_hour_now()
print(data.get_just_date())"""

