def get_temperature():
    while True:
        temperature_str = input("Please enter the temperature in Fahrenheit: ")
        try:
            temperature = float(temperature_str)
            return temperature
        except ValueError:
            print("Error: Please enter a valid numerical value for temperature.")

def main():
    temperature = get_temperature()
    print("Temperature entered:", temperature)

if __name__ == "__main__":
    main()
    
    
    



def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except Exception as e:
        print("An error occurred during the conversion:", e)

# Example usage:
temperature_fahrenheit = 75
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
if temperature_celsius is not None:
    print(f"{temperature_fahrenheit}°F is equal to {temperature_celsius:.2f}°C")