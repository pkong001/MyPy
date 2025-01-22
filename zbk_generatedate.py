from datetime import datetime, timedelta

# Start and end dates
start_date_str = "2018-01-01"
end_date_str = "2023-12-01"

# Convert strings to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# Initialize current date to the start of the next month
current_date = start_date.replace(day=1) #+ timedelta(days=31)
current_date_2 = (current_date + timedelta(days=31)) #บางที่อาจต้องเปลี่ยนวันตรงนี้ถ้าเลขของเดือนแรกไม่ลงตัว
end_date_2 = end_date.replace(day=1) + timedelta(days=31)
current_date = current_date.replace(day=1)

# Generate dates
dates = []
while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    # Move to the next month
    current_date += timedelta(days=31)
    current_date = current_date.replace(day=1)

dates2 = []
while current_date_2 <= end_date_2:
    dates2.append(current_date_2.strftime("%Y-%m-%d"))
    # Move to the next month
    current_date_2 += timedelta(days=31)
    current_date_2 = current_date_2.replace(day=1)

# Concatenate pair by pair
concatenated_dates = [f"'{d1}' '{d2}'" for d1, d2 in zip(dates, dates2)]

# print(dates)
# print(dates2)
print(concatenated_dates)


concatenated_dates_list = [(d1, d2) for d1, d2 in zip(dates, dates2)]

print(concatenated_dates_list)

concatenated_dates_list = [(d1, d2) for d1, d2 in zip(dates, dates2)]
concatenated_dates_list.reverse()
for d1, d2 in concatenated_dates_list:
    print(f"'{d1}' '{d2}'")
