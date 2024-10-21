# Declarations
allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
menuOptions = ['PRINT all Authorized Vehicles']

def display_menu(menuOptions):
    # Print the menu header
    print()
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print("********************************")
    print()
    # Print the menu options
    print('Please Enter the following number below from the following menu:')
    print()
    #add exit to the end of menuOptions
    for index, menuOption in enumerate (menuOptions + ['Exit']):
        #Display each option with its index number
        print(f'  {index + 1}. {menuOption}')

def print_authorized_vehicles(allowedVehiclesList):
    # Inform the user of authorized vehicles
    print('    The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    print()
    # Loop through the list of allowed vehicles and print each one
    for allowedVehicle in allowedVehiclesList:
        print(f'      {allowedVehicle}')


def main():
    # Start a loop to display the menu and process user input
    while True:
        print()
        # Call function to display the menu
        display_menu(menuOptions)
        print()

        # Get user input for menu selection
        response = input('Option:  ')
        print()

        try:
            # Convert the user input to an interger
            response = int(response) 

            # Check if the user selected the "Exit" option
            if response == len(menuOptions) + 1:
                # Print a goodbye message and exit the program
                print('  Thank you for using the AutoCountry VehicleFinder, good-bye!')
                break

            # If the user selected a valid menu option
            elif 1 <= response <= len(menuOptions):
                print('You selected the following option:')
                print()

                # Print the selected option with quotation marks
                print(f'  "{response}. {menuOptions[response - 1]}"')
                print()

                # If the user selected the first option, print the authorized vehicles
                if response == 1:
                    print_authorized_vehicles(allowedVehiclesList)
            
            # Handle case where the user selects an unavailable option
            else:
                print(f'Option {response} is not currently available.')
                print('Please try again.')
        except ValueError:
            # Handle case where the user input is not a valid interger
            print(f'"{response}" is an invalid response.')
            print('Please try again.')

# Entry point of the program   
if __name__ == "__main__":
    main()