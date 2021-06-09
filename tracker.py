from datetime import datetime
import csv

def getLimit():
    with open("contributions.csv") as rf:
        csvFile = list(csv.reader(rf))
        totalRows = len(csvFile)-1
        print(csvFile)
        currentLimit = float(csvFile[totalRows][2])
    return currentLimit

def enterContribution(amount, addLimit = 0, overwriteLimit = False):
    with open("contributions.csv", "a") as recordFile:
        if overwriteLimit:
            newLimit = input("Enter new contribution limit: ")
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{newLimit}\n")
        else:
            recordFile.write(f"{datetime.today().strftime('%Y-%m-%d')},{amount},{getLimit()-amount+addLimit}\n")


enterContribution(9999, overwriteLimit = True)


