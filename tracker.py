from datetime import datetime
import csv
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
        lastContributed = csvFile[totalRows][0]
        lastContribution = csvFile[totalRows][1]
    return getLimit(), lastContributed, lastContribution


def enterContribution(amount, addLimit = 0, overwriteLimit = False):
    with open("contributions.csv", "a") as recordFile:
        if overwriteLimit:
            newLimit = input("Enter new contribution limit: ")
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{newLimit}\n")
        else:
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{getLimit()-amount+addLimit}\n")


def main():  
    print("\nStatus:\n\nCurrent contribution limit: $ %s\nLast contribution date: %s\nLast contribution amount: $ %s\n"%(getStatus()[0], getStatus()[1],getStatus()[2]))        

    while True:
        confirmation = input("Would you like to make a contribution today? [Y/N]: ")
        if confirmation.lower() == "y":
            while True:
                update = input("Would you like to update your contribution limit first? [Y/N]: ")
                if update.lower() == "y":
                    updateOption = input("1) Add an amount to current contribution limit\n2)Overwrite and update total contribution limit\n")
                    while True:
                        if updateOption == "1":
                            addLimit = float(input("Enter limit increase amount: "))
                            break
                        elif updateOption == "2":
                            overwriteLimit = True
                            break
                elif update.lower() == "n":
                    addLimit = 0
                    overwriteLimit = False
                    break
            contributionAmount = float(input("How much are you contributing? "))
            enterContribution(contributionAmount, addLimit = addLimit, overwriteLimit = overwriteLimit)
            break
        elif confirmation.lower() == "n":
            print("\nI see. See you next time.\n")
            break
if __name__ == "__main__":
    main()
