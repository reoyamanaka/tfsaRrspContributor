from datetime import datetime
import csv, os
from pprint import pprint


def getLimit():
    with open("contributions.csv") as rf:
        csvFile = list(csv.reader(rf))
        totalRows = len(csvFile)-1 
        currentLimit = float(csvFile[totalRows][2])
    return currentLimit


def getStatus():
    with open("contributions.csv") as rf:
        csvFile = list(csv.reader(rf))
        totalRows = len(csvFile) - 1

        if totalRows < 1:
            return False

        lastContributed = csvFile[totalRows][0]
        lastContribution = csvFile[totalRows][1]
    return getLimit(), lastContributed, lastContribution


def enterContribution(amount, addLimit = 0, overwriteLimit = False):
    with open("contributions.csv", "a") as recordFile:
        if overwriteLimit:
            newLimit = input("Enter new contribution limit AFTER contributing the $ %s: "%amount)
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{newLimit}\n")
        else:
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{getLimit()-amount+addLimit}\n")


def main():
    if not os.path.exists(os.getcwd()+"/contributions.csv"):
        with open("contributions.csv", "w") as wf:
            wf.write("date,amount,contributionLimit\n")
            initialContribution = float(input("Enter current contribution limit: "))
            wf.write(f"N/A,N/A,{initialContribution}\n")
                
    if getStatus(): 
        print("\nStatus:\n\nCurrent contribution limit: $ %s\nLast contribution date: %s\nLast contribution amount: $ %s\n"%(getStatus()[0], getStatus()[1],getStatus()[2]))        
    overwriteLimit = False
    addLimit = 0
    while True:
        confirmation = input("Would you like to make a contribution today? [Y/N]: ")
        if confirmation.lower() == "y":
            while True:
                update = input("Would you like to update your contribution limit? [Y/N]: ")
                if update.lower() == "y":
                    updateOption = input("1) Add an amount to current contribution limit\n2) Overwrite and update total contribution limit\n")
                    while True:
                        if updateOption == "1":
                            addLimit = float(input("Enter limit increase amount: "))
                            break
                        elif updateOption == "2":
                            overwriteLimit = True
                            print("I see. Please enter your contribution amount first, and then you will be asked to enter the latest contribution limit.\n")
                            break 
                    break
                elif update.lower() == "n":
                    break
            contributionAmount = float(input("How much are you contributing? "))
            enterContribution(contributionAmount, addLimit = addLimit, overwriteLimit = overwriteLimit)
            break
        elif confirmation.lower() == "n":
            print("\nI see. See you next time.\n")
            break
if __name__ == "__main__":
    main()
