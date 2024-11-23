##This application will allow users to find a list of 
##vehicles for sale within AutoCountry

##Here is the file list for the vehicles
allowedVehicleList =  ['Ford F-150' , 'Chevrolet Silverado' , 'Tesla Cybertruck' , 'Toyota Tundra' , 'Rivian R1T' , 'Ram 1500']

##Write the initial vehicle list to the file
with open('allowedVehicleList.txt', 'w') as tfile:
    tfile.write('\n'.join(allowedVehicleList))

##Open application prompt
prompt = ("******************************** \nAutoCountry Vehicle Finder v1.0 \n********************************" 
          "\nPlease Enter the following number below from the following menu: \n1. PRINT all Authorized Vehicles "
          "\n2. SEARCH all Authorized Vehicles \n3. ADD Authorized Vehicle \n4. Delete Authorized Vehicle \n5. Exit")


##Convert all prompt elif statements to clear defined functions

##Function and statement for all vehicle printing
def Print_Auth_Vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    with open('allowedVehicleList.txt', 'r') as tfile:
        for line in tfile:
            print(f"- {line.strip()}")

##Function and statement to search for a vehicle
def Search_All_Vehicle():
    print("******************************** \nPLEASE ENTER THE FULL VEHICLE NAME ")
    searchVehicle = input("")
    with open('allowedVehicleList.txt', 'r') as tfile:
        allowedVehicleList = [line.strip() for line in tfile]
    if searchVehicle in allowedVehicleList:
        print(f"{searchVehicle} is an authorized vehicle")
    else:
        print(f"{searchVehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")

##Function and statement to add a vehicle to the list
def Add_to_list():
    print("******************************** \nPlease Enter the full Vehicle name you would like to ADD: ")
    newVehicle = input("")
    with open('allowedVehicleList.txt', 'r') as tfile:
        allowedVehicleList = [line.strip() for line in tfile]
    if newVehicle not in allowedVehicleList:
        with open('allowedVehicleList.txt', 'a') as tfile:
            tfile.write(f"{newVehicle}\n")
        print(f"You have added {newVehicle} to the authorized vehicle list.")
    else:
        print(f"{newVehicle} is already in the authorized vehicle list.")

##Function and statements to remove a vehicle from the list
def Remove_from_list():
    print("******************************** \nPlease Enter the full Vehicle name you would like to REMOVE: ")
    outdatedVehicle = input("")
    with open('allowedVehicleList.txt', 'r') as tfile:
        allowedVehicleList = [line.strip() for line in tfile]
    if outdatedVehicle in allowedVehicleList:
        print(f"Are you sure you want to remove {outdatedVehicle} from the Authorized Vehicles List?")
        removeConfirm = input("").lower()
        if removeConfirm == 'yes':
            allowedVehicleList.remove(outdatedVehicle)
            with open('allowedVehicleList.txt', 'w') as tfile:
                tfile.write('\n'.join(allowedVehicleList) + '\n')
            print(f"You have removed {outdatedVehicle} from the authorized vehicle list.")
        else:
            print("The vehicle was not removed.")
    else:
        print(f"{outdatedVehicle} is not in the authorized vehicle list.")

##Corrected while statement for loop      
while True:
    print(prompt)
    answer = input("select: ")

##Created If statements for user selections within prompt loop
    if answer == '1':
        Print_Auth_Vehicles()
    elif answer == '2':
        Search_All_Vehicle()  
    elif answer == '3':
        Add_to_list()  
    elif answer == '4':
        Remove_from_list() 
##End application
    elif answer == '5':
        print("******************************** \nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break