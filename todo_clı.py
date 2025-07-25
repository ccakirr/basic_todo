from datetime import datetime
date = datetime.now()
current_date = date.date()

def save_completed_task(task):
    try:
        file = open(f"{current_date}_dids.txt", "x")
    except FileExistsError:
        file = open(f"{current_date}_dids.txt", "a")
    file.write(str(task) + "\n")
    print("\nTask saved to history.")
    file.close()

def del_completed_task(missions, compmissions):
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
        save_completed_task(compmissions[comp])
        print(f"Mission {comp} completed!")
        print(f"You have {len(missions)} mission(s) left.")
        break

def show_missions(missions, compmissions):
    print("\nMissions left:")
    for key, value in missions.items():
        print(f"{key}. {value}")
    if compmissions:
        print("\nCompleted missions:")
        for key, value in compmissions.items():
            print(f"{key}. {value}")

def main():
    countofmis = int(input("Please enter the count of today's missions.\n"))
    i = 1
    missions = {}
    compmissions = {}
    while i <= countofmis:
        missions[i] = input(f"Please enter the {i}. mission.\n")
        i = i + 1
    while missions:
        show_missions(missions, compmissions)
        del_completed_task(missions, compmissions)
    print(f"Congratulations! You have completed all missions!\nYou can reach your history from same file with this application. They saved to {current_date}_dids.txt")

main()