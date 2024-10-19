

import calendar
from datetime import datetime

def display_months_and_date(year):
    output = f"\nMonths in the year {year}:\n"
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        output += month_name + "\n"
    
    today = datetime.now()
    if today.year == year:
        output += f"Current date: {today.strftime('%B %d, %Y')}\n"
    
    return output


def main():
    while True:
        try:
            user_input = input("Enter 1 to select a single year, or 2 or 3 years separated by commas (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            
            year_strings = user_input.split(',')
            years = [int(year.strip()) for year in year_strings]

            if len(years) < 1 or len(years) > 100:
                print("select the year")
                continue
            
            for year in years:
                display_months_and_date(year)

        except ValueError:
            print("Please enter valid years.")

if __name__ == "__main__":
    main()
