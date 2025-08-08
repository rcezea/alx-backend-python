from datetime import datetime

# Step 1: Set an old time (e.g., 2 hours and 45 minutes ago)
old_time = datetime(2025, 8, 5, 10, 0)  # YYYY, MM, DD, HH, MM

# Step 2: Get the current time
now = datetime.now()

# Step 3: Calculate the difference
diff = now - old_time

# Step 4: Convert the difference into total minutes
total_minutes = int(diff.total_seconds() // 60)
hours = total_minutes // 60
minutes = total_minutes % 60
seconds = int(diff.total_seconds() % 60)

print(f"Time difference: {hours} hours,  {minutes} minutes and {seconds} seconds")
