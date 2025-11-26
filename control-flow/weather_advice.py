user = input("What's the weather like today? (sunny/rainy/cold): ")
if user == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif user == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif user == 'cold':
    print("Wear a warm jacket and a scarf.")    
else:
    print("Sorry, I don't have advice for that weather condition.")