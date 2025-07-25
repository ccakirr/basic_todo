from datetime import datetime
date = datetime.now()
current_date = date.date()
def savecomplated(task):
    try:
        file = open(f"{current_date}_dids.txt", "x")
    except FileExistsError:
        file = open(f"{current_date}_dids.txt", "a")
    file.write(str(task) + "\n")
    file.close()
    
def delcomplated(missions, compmissions):
    while True:
        try:
            comp = int(input("\nPlease enter the completed mission's number:\n"))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if comp not in missions:
            print("Please enter a valid mission number.\n")
            continue
        compmissions[comp] = missions[comp]
        missions.pop(comp)
        savecomplated(compmissions[comp])
        print(f"Mission {comp} completed!\n")
        break

def main():
    countofmis = int(input("Please enter the count of today's missions.\n"))
    i = 1
    missions = {}
    compmissions = {}
    while i <= countofmis:
        missions[i] = input(f"Please enter the {i}. mission.\n")
        i = i + 1
    while missions:
        print("\nMissions left:")
        for key, value in missions.items():
            print(f"{key}. {value}")
        if compmissions:
            print("\nComplated missions:")
            for key, value in compmissions.items():
                print(f"{key}. {value}")
        delcomplated(missions,compmissions)
    print("Congratulations you have done all missions!\n")

main()