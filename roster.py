# https://goheels.com/sports/mens-basketball/roster

import pandas as pd


player = {"Last Names": ["Bacot", "Davis", "Cadeau", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"
            ],
          "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Rob"
            ],
          "Height": [83, 72, 73, 81, 77, 75, 77, 82, 73, 79],
          "Weight": [240, 180, 180, 225, 195, 195, 195, 230, 180, 200], }

data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters^2
data["BMI"] = (data["Weight"] / 2.205) / ((data["Height"] / 39.37) ** 2)

data["BMI"] = data["BMI"].round(2)

print(data)
