from datetime import datetime, timedelta

# 1️ Subtract five days from current date
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("1) Current date:", current_date)
print("   Date minus 5 days:", new_date)


# 2️ Print yesterday, today, tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\n2) Yesterday:", yesterday.date())
print("   Today:", today.date())
print("   Tomorrow:", tomorrow.date())


# 3️ Drop microseconds from datetime
now_with_microseconds = datetime.now()
without_microseconds = now_with_microseconds.replace(microsecond=0)

print("\n3) Datetime with microseconds:", now_with_microseconds)
print("   Datetime without microseconds:", without_microseconds)


# 4️ Calculate difference between two dates in seconds
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("\n4) Difference between two dates in seconds:", seconds)