# Declarations
allowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
menuOptions = ['PRINT all Authorized Vehicles', 'SEARCH for Authorized Vehicle', 'ADD Authorized Vehicle', 'DELETE Authorized Vehicle', 'RESET/RESTORE Authorized Vehicle List']
authorizedVehicles = "Authorized_Vehicle_File.txt"

def display_menu(menuOptions):
    
    ## Display header and menu options
    ## Appends exit to end of options
    
    print()
    print('********************************')
    print('AutoCountry Vehicle Finder v1.0')
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
            
            # Close File
            db.close()

def print_authorized_vehicles(authorizedVehicles):
    
    ## Print all authorized vehicle in file
    import os
    with open(authorizedVehicles, 'r') as db:
        vehicles = db.readlines()
        
        #Strip away extra whitespace 
        vehicles = [vehicle.strip() for vehicle in vehicles]
        
        # Inform the user of authorized vehicles
        print('    The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        print()
        
        # Print each vehicle on a separate line
        for vehicle in vehicles:
            print(f'      {vehicle}')
        
        # Close File
        db.close()

def print_searched_vehicles(authorizedVehicles):
    
    # Allow user to search authorized vehicles
    # Warn user that make and model must be entered
    
    print('\033[1mPlease ENTER the full Vehicle name you would like to search:\033[0m')
    print()
    
    # Get user input for search criteria
    search = input('Search for this vehicle: ')
    print ()
    
    # read vehicles from file
    import os

    with open(authorizedVehicles, 'r') as db:
        vehicles = db.readlines()
        vehicles = [vehicle.strip() for vehicle in vehicles]
        
        # Check and print results for no matching vehicles
        if search not in vehicles:
            print(f'{search} is not an authorized vehicle, if you received this in error please check the spelling and try again.')
            
        # Print results for matching vehicles
        else:
            print(f'{search} is an authorized vehicle.')
        
        # Close file
        db.close
        
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
    
    # Open Vehicle File with read/write permission
    with open(authorizedVehicles, "r+") as db:
        vehicles = db.readlines()
        vehicles = [vehicle.strip() for vehicle in vehicles]
    
        # Check if vehicles is in list before adding
        if update not in vehicles:
            db.write (update + "\n")
            print (f'"{update}" has been added to the Authorized Vehicles List.')
            print(f'\033[1mYou have added "{update}" as an authorized vehicle.\033[0m') 
        
       # Notify user vehicle to add is already in file 
        else:
            print (f'"{update}" is already in the Authorized Vehicles List')
        db.close()

def remove_authorized_vehicles_file (authorizedVehicles):
    
    ## Allow user to remove vehicles to file
    
    print('\033[1mPlease ENTER the full Vehicle name you would like to REMOVE:\033[0m')
    print()
    
    # Request user input
    while True:
        removal = input('Update to remove:  ')
        
        # check if user did not enter value
        if removal:
            break
        print ("Input not entered.  Please try again.")

    # Read vehicles in file
    with open(authorizedVehicles, "r+") as db:
        vehicles = db.readlines()
        vehicles = [vehicle.strip() for vehicle in vehicles]

        # Check if requested vehicle is listed in file
        if removal not in vehicles:
            
            # Notify user if vehicle is not in file
            print(f'"{removal}" is not in the Authorized Vehicle List.')
            return    

        # If vehicle in file, confirm request to remove before removing
        else:
            while True:
                confirm = input(f'** Are you sure you want to remove {removal} from the Authorized Vehicles List?  ')
    
                # Display error if value other than 'yes' or 'no' has been entered
                if confirm.lower() not in ['yes', 'no']:
                    print(f'{confirm} is Invalid response. Please enter "yes" or "no".')
                
                # Repeat confirmation loop if invalid value was entered
                else:
                    break                
                
            # Return to main menu if user responds 'no'
            if confirm.lower() == 'no':
                print("Vehicle removal cancelled.")
                return
                
            # Remove vehicle from the list if user responds 'yes'
            elif confirm.lower() == 'yes':
                vehicles.remove(removal)

                # Clear list before updating
                db.seek(0)
                db.truncate()

                # Write the updated list to the file
                for vehicle in vehicles:
                    db.write (vehicle + "\n")

                # Display confirmation messages    
                print (f'"{removal}" has been deleted from the Authorized Vehicles List.')
                print(f'\033[1mYou have removed "{removal}" as an authorized vehicle.\033[0m')
        
        # Close File
        db.close

def reset_authorized_vehicles_file (authorizedVehicles):
    
    ## Reset file to the predefined list
    ## Overwrites any previous changes made to file

    # Display warning
    print(f'\033[1mYou are attempting to {menuOptions[4]}.\033[0m')
    print('\033[1mThis will restore the the Authorized Vehicle List to original.\033[0m')
    print('\033[1mAny changes previously made will be lost.\033[0m')
    print()

    # Request user confrimation before continuing
    reset = input('Are you sure you wish to proceed? (Yes/No): ').strip().lower()

    # Proceed with reset
    if reset == 'yes':

        # open vehicle list file with write permissions
        with open(authorizedVehicles, 'w') as db:
                
            # Overwrite current list and replace with list in "allowedVehiclesList"
            for vehicle in allowedVehiclesList:
                
                # Write each vehicle on a separate line with a new line for future entries
                db.write(vehicle + "\n")
                
            # Close file
            db.close
        print (f'"Authorized Vehicles List has been restored to original.')
    
    else:
        print(f"{menuOptions[4]} cancelled.")














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
                # Option 4: delete authorized vehicles
                elif response == 4:
                    remove_authorized_vehicles_file(authorizedVehicles)
                
                # Option 5: Clear all changes and reset default vehicle list
                elif response == 5:
                    reset_authorized_vehicles_file (authorizedVehicles)

            
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