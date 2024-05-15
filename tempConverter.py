# function for converting Celsius to Fahrenheit
def celsiusToFahrenheit(temperature):
    return (temperature * 9/5) + 32

# function for converting Fahrenheit to Celsius
def fahrenheitToCelsius(temperature):
    return (temperature - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")

    # while loop to repeat until user doesn't want to play again
    while True:
        choice = input("Do you want to enter a temperature in Celsius or Fahrenheit? (C/F) ")
        
        if choice == 'c' or choice == 'C': # converts Celsius to Fahrenheit
            user_temperature = float(input("Please enter a temperature: ")) # ask user to enter temperature
            new_temperature = celsiusToFahrenheit(user_temperature)
            rounded_temperature = round(new_temperature, 1)
            print(str(user_temperature) + " Celsius is " + str(rounded_temperature) + " Fahrenheit!")
        elif choice == 'f' or choice == 'F': # converts Fahrenheit to Celsius
            user_temperature = float(input("Please enter a temperature: ")) # ask user to enter temperature
            new_temperature = fahrenheitToCelsius(user_temperature)
            rounded_temperature = round(new_temperature, 1)
            print(str(user_temperature) + " Fahrenheit is " + str(rounded_temperature) + " Celsius!")
        else: # Prompt user to enter valid chocie
            print("Please enter 'C' or 'F': ")
            continue
        
        # Ask user if they want to play again
        user_repeat = input("Do you want to play again? (y/n) ").lower()
        if user_repeat != 'y':
            print("Thank you for playing the Temperature Converter!")
            break

if __name__ == "__main__":
    main()