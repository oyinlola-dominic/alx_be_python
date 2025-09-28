# Ask user for the weather 
weather = input("What's the weather like today (sunny, rainy, snowycold): ").lower()
# Give clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a rain coat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry I don't have a recommendation for this weather.")
    