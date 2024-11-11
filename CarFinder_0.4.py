# Declarations
allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
menuOptions = ['PRINT all Authorized Vehicles', 'SEARCH for Authorized Vehicle', 'ADD Authorized Vehicle', 'DELETE Authorized Vehicle']
authorizedVehicles = "Authorized_Vehicle_File.txt"

def display_menu(menuOptions):
    
    ## Display header and menu options
    ## Appends exit to end of options
    
    print()
    print('********************************')
    print('AutoCountry Vehicle Finder v0.2')
    print("********************************")
    print()
    print('Please Enter the following number below from the following menu:')
    print()
    
    #add exit to the end of menuOptions
    for index, menuOption in enumerate (menuOptions + ['Exit']):
    
        #Display each option with its index number
        print(f'  {index + 1}. {menuOption}')

def create_authorized_vehicles_file (authorizedVehicles):
    
    ## Create file if it does not exist
    ## Writes predefined input into file
    
    import os
    if not os.path.isfile(authorizedVehicles):
    
        # If file does not exist, create it and add extra line
        with open(authorizedVehicles, 'w') as db:
            for vehicle in allowedVehiclesList:
                db.write(vehicle + "\n")

def print_authorized_vehicles(authorizedVehicles):
    
    ## Print all authorized vehicle in file
    ## If fil
    
    import os
    if os.path.isfile(authorizedVehicles):
        with open(authorizedVehicles, 'r') as db:
            vehicles = db.readlines()
    
            #Strip away extra whitespace 
            vehicles = [vehicle.strip() for vehicle in vehicles]
    else:
        vehicles = []
    
    # Inform the user of authorized vehicles
    print('    The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    print()
    
    # Print each vehicle on a separate line
    for vehicle in vehicles:
        print(f'      {vehicle}')

def print_searched_vehicles(authorizedVehicles):
    
    # Allow user to search authorized vehicles
    # Warn user that make and model must be entered
    
    print('\033[1mPlease ENTER the full Vehicle name you would like to search:\033[0m')
    print()
    
    # Get user input for search criteria
    search = input('Search for this vehicle: ')
    print ()
    
    # read vehicles from file and search for input vehicle
    import os
    if os.path.isfile(authorizedVehicles):
        with open(authorizedVehicles, 'r') as db:
            vehicles = db.readlines()
            vehicles = [vehicle.strip() for vehicle in vehicles]
    
    # Check and print results for matching vehicles
    if search in vehicles:
        print(f'{search} is an authorized vehicle.')
    else:
        print(f'{search} is not an authorized vehicle, if you received this in error please check the spelling and try again.')

def append_authorized_vehicles_file (authorizedVehicles):
    
    ## Allow user to add vehicles to file
    ## Prevents duplicate entries
    
    print('\033[1mPlease ENTER the full Vehicle name you would like to add:\033[0m')
    print()
    
    # Get user input to update list
    while True:
        update = input('Update to include:  ')
        if update:
            break
        print ("Input not entered.  Please try again.")
    
    # Read vehicles in file
    with open(authorizedVehicles, "r") as db:
        vehicles = db.readlines()
        vehicles = [vehicle.strip() for vehicle in vehicles]
    
    # Check if vehicles is in list before adding
    if update not in vehicles:
        with open (authorizedVehicles, 'a') as db:
            db.write (update + "\n")
            db.close
        print (f'"{update}" has been added to the Authorized Vehicles List.')
        print(f'\033[1mYou have added "{update}" as an authoriezed vehicle.\033[0m')
    else:
        print (f'"{update}" is already in the Authorized Vehicles List')

def remove_authorized_vehicles_file (authorizedVehicles):
    
    ## Allow user to add vehicles to file
    ## Prevents duplicate entries
    
    print('\033[1mPlease ENTER the full Vehicle name you would like to REMOVE:\033[0m')
    print()
    
    # Get user input to update list
    while True:
        removal = input('Update to remove:  ')
        if removal:
            break
        print ("Input not entered.  Please try again.")

    # Read vehicles in file
    with open(authorizedVehicles, "r") as db:
        vehicles = db.readlines()
        vehicles = [vehicle.strip() for vehicle in vehicles]
    
    # Check if vehicles is in list before removing
    if removal in vehicles:

        #Ask for confirmation to remove
        while True:
            confirm = input(f'** Are you sure you want to remove {removal} from the Authorized Vehicles List?  ')
            if confirm.lower() == 'yes':

                # Remove vehicle from the list
                vehicles.remove(removal)

                with open (authorizedVehicles, 'w') as db:
                    for vehicle in vehicles:
                        db.write (vehicle + "\n")
                print (f'"{removal}" has been deleted from the Authorized Vehicles List.')
                print(f'\033[1mYou have removed "{removal}" as an authoriezed vehicle.\033[0m')
                break
            elif confirm.lower() == 'no':
                print("Vehicle removal cancelled.")
                break
            elif confirm == "":
                print("No response entered.  Please confirm deletion by entering 'yes' or 'no'. ")
            else:
                print ('Invalid response. Please enter "yes" or "no".')
    else:
        print(f'"{removal}" is not in the Authorized Vehicle List.')

def reset_authorized_vehicles_file (authorizedVehicles):
    
    ## Reset file to the predefined list
    ## Overwrites any changes made to file
    
    import os
    if os.path.isfile(authorizedVehicles):
    
        # read file contents
        with open(authorizedVehicles, 'r') as db:
            vehicles = db.readlines()
            vehicles = [vehicle.strip() for vehicle in vehicles]
    
        # only reset if file does not match predefined list
        if vehicles == allowedVehiclesList:
            return
    
    # reset file
    with open(authorizedVehicles, 'w') as db:
        for vehicle in allowedVehiclesList:
            db.write(vehicle + "\n")

def main():

    ## Main function to run program
    ## Provides menu for user interaction

    create_authorized_vehicles_file (authorizedVehicles)
    
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

                ###  Optional functionality ###
                #reset_authorized_vehicles_file (authorizedVehicles)

    
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

                # Option 1: print the authorized vehicles
                if response == 1:
                    print_authorized_vehicles(authorizedVehicles)
                
                # Option 2: search authorized vehicles
                elif response == 2:
                    print_searched_vehicles(authorizedVehicles)
                
                # Option 3: add authorized vehicles
                elif response == 3:
                    append_authorized_vehicles_file(authorizedVehicles)
                # Option 3: add authorized vehicles
                elif response == 4:
                    remove_authorized_vehicles_file(authorizedVehicles)
            
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