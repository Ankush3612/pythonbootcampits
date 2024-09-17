from datetime import datetime

def days_between_dates(birthdate_str):
    """
    Calculates the number of days between the given birthdate and today.
    """
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.today()
        delta = today - birthdate
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Example usage:
user_birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
days = days_between_dates(user_birthdate)
if isinstance(days, int):
    print(f"Congratulations! You've been alive for approximately {days} days.")
else:
    print(days)