from datetime import datetime
import csv, os
from pprint import pprint


def getLimit():
    with open("contributions.csv") as rf:
        csvFile = list(csv.reader(rf))
        totalRows = len(csvFile)-1 
        if totalRows < 1:
            return 0
        currentLimit = float(csvFile[totalRows][2])
    return currentLimit


def updateLimit(newLimit):
    with open("contributions.csv", "a") as recordFile:
        recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},0,{newLimit}\n")        
    return None


def getStatus():
    with open("contributions.csv") as rf:
        csvFile = list(csv.reader(rf))
        totalRows = len(csvFile) - 1

        if totalRows < 1:
            return False

        lastContributed = csvFile[totalRows][0]
        lastContribution = csvFile[totalRows][1]
    return getLimit(), lastContributed, lastContribution


def enterContribution(amount, addLimit = 0):
    with open("contributions.csv", "a") as recordFile:
        recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{getLimit()-amount+addLimit}\n")
    return None


def main():
    if not os.path.exists(os.getcwd()+"/contributions.csv"):
        with open("contributions.csv", "w") as wf:
            wf.write("date,amount,contributionLimit\n")
            initialContribution = float(input("Enter current contribution limit: "))
            wf.write(f"N/A,N/A,{initialContribution}\n")                
    if getStatus(): 
        print("\nStatus:\n\nCurrent contribution limit: $ %s\nLast contribution date: %s\nLast contribution amount: $ %s"%(getStatus()[0], getStatus()[1],getStatus()[2]))        
    overwriteLimit = False
    addLimit = 0
    while True:
        confirmation = input("\nWould you like to make a contribution today? [Y/N]: ")
        if confirmation.lower() == "y":
            while True:
                update = input("\nWould you like to update your contribution limit first? [Y/N]: ")
                if update.lower() == "y":
                    updateOption = input("1) Add an amount to current contribution limit\n2) Overwrite and update total contribution limit\n")
                    while True:
                        if updateOption == "1":
                            addLimit = float(input("Enter limit increase amount: "))
                            break
                        elif updateOption == "2":
                            updatedLimit = float(input("Enter updated contribution limit: "))
                            updateLimit(updatedLimit)
                            break
                        else:
                            print("\nInvalid input. Please enter 1 or 2: ") 
                    break
                elif update.lower() == "n":
                    break
                else:
                    print("\nInvalid input. Please enter 'Y' or 'N' (case-insensitive): ")
            contributionAmount = float(input("How much are you contributing? "))
            enterContribution(contributionAmount, addLimit = addLimit)
            break
        elif confirmation.lower() == "n":
            print("\nI see. See you next time.\n")
            break
        else:
            print("\nInvalid input. Please enter 'Y' or 'N' (case-insensitive): ")
if __name__ == "__main__":
    main()
