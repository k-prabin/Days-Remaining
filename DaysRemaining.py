from datetime import datetime

def days_remaining(from_date):
    # Convert the input date string to a datetime object
    from_date = datetime.strptime(from_date, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in days
    remaining_days = (from_date - current_date).days

    return remaining_days

# Set the desired date directly in the code (YYYY-MM-DD format)
desired_date = "2024-12-31"

# Calculate and print the remaining days
remaining_days = days_remaining(desired_date)
print(f"Days remaining from {desired_date} to today: {remaining_days} days")
