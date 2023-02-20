import datetime

# Get current date
current_date = datetime.date.today()

# Subtract five days
new_date = current_date - datetime.timedelta(days=5)

print("Current date:", current_date)
print("New date:", new_date)
