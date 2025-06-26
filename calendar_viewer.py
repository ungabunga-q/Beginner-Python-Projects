"""
Calendar Viewer
Displays a calendar for a given month and year.
"""
import calendar

def show_calendar(year, month):
    print(calendar.month(year, month))

if __name__ == "__main__":
    y = int(input("Enter year: "))
    m = int(input("Enter month: "))
    show_calendar(y, m)
