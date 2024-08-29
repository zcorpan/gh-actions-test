from datetime import datetime

# Get the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Define the content to write to index.html
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <p>{current_datetime}</p>
</body>
</html>
"""

# Write the content to index.html
with open("index.html", "w") as file:
    file.write(html_content)

print("index.html has been updated.")
