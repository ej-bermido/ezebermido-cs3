#2 BERMIDO, Ezekiel Javier L.
#9 - Pinatubo

def chinese_zodiac(birth_year):

    num = (birth_year - 1900) % 12
    zodiacs = ['Rat (鼠 / Shǔ)', 'Ox (牛 / Niú)', 'Tiger (虎 / Hǔ)', 'Rabbit (兔 / Tù)', 'Dragon (龙 / Lóng)', 'Snake (蛇 / Shé)', 'Horse (马 / Mǎ)', 'Goat (羊 / Yáng)', 'Monkey (猴 / Hóu)', 'Rooster (鸡 / Jī)', 'Dog (狗 / Gǒu)', 'Pig (猪 / Zhū)'  ]
    result = zodiacs[num]
    return result
    
try:
    year_of_birth = int(input("Enter your birth year ::: "))
    
    if year_of_birth < 1900:
        print("Yo you're too old!!! PPlease input a valid birth year")
    
    else:
        zodiac = chinese_zodiac(year_of_birth)
        print(f"Your Chinese Zodiac sign is ::: {zodiac}")

except Exception:
    print("Yo you're too old!!! Please input a valid birth year and restart the program.")
    
