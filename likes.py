import json
import secrets
import os
from PIL import Image, ImageDraw, ImageFont

list = []
with open('likers.json', 'r', encoding="utf8") as file:
    likes = json.load(file)
    list += likes['users']

with open('likers2.json', 'r', encoding="utf8") as file:
    likes2 = json.load(file)
    list += likes2['users']

index = secrets.randbelow(len(list))
print(index)
winner = list[index]
print(fr"Full name: {winner['full_name']}, Username: {winner['username']}")

width, height = 800, 600
img = Image.new('RGB', (width, height), color='#b9dca9')
imgDraw = ImageDraw.Draw(img)

message = f"{winner['full_name']}" if len(winner['full_name']) > 0 else f"@{winner['username']}"
message2 = f"@{winner['username']}" if len(winner['full_name']) > 0 else ""
font = ImageFont.truetype("arial.ttf", size=72)
font2 = ImageFont.truetype("arial.ttf", size=48)
bbox = imgDraw.textbbox((0, 0), message, font=font)
textWidth = bbox[2] - bbox[0]
textHeight = bbox[3] - bbox[1]
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2
imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 255))
imgDraw.text((xText, yText + 80), message2, font=font2, fill=(255, 255, 255))
img.save("winner.png")
os.startfile("winner.png")