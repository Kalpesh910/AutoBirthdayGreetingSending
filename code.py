import pandas as pd
import datetime
from PIL import Image, ImageFont, ImageDraw
# Data reading
data = pd.read_excel("team_birthdays.xlsx")

# Get today's day and month
today = datetime.date.today()
today_month_day = today.strftime("%m-%d")

# Extract day and month from the "Birthday" column
data["Birthday_month_day"] = data["Birthday"].dt.strftime("%m-%d")

# Identify upcoming birthdays
birthday_guys = data[data["Birthday_month_day"] == today_month_day]

# Font of the Name
font = ImageFont.truetype("Requirements/Caveat/static/Caveat-Bold.ttf", 124)

# Checking the bithday_guys
for _, group in birthday_guys.groupby("Birthday_month_day"):
    
    for _, row in group.iterrows():
        
        # background Image
        img = Image.open("bgPoster.png")
        
        # Name of the birthday guy
        name = row["Name"].split()[0]
        
        # Photo of the birthday guy
        photo = Image.open(row["Photo"])
        
        # Adding the text on background image
        draw = ImageDraw.Draw(img)
        draw.text((390, 1600), name, (61,80,84), font=font)

        # Adding the photo on background image    
        photo_position = (205, 550, 875, 1230)
        photo = photo.resize((photo_position[2]-photo_position[0], photo_position[3]-photo_position[1]))
        img.paste(photo, photo_position)
        
        # Poster is ready saving it to 
        img.save("Poster/" + name + "_wish.png")