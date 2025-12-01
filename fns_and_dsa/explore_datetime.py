from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    
    # Format and display the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

    return current_date  # Return so it can be reused


def calculate_future_date(current_date, days_to_add):
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)

    # Format future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)

    return future_date


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input! Please enter an integer number of days.")


if __name__ == "__main__":
    main()
