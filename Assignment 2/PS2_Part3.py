beginningOdometerReading = int(input("Please enter the beginning odometer reading: "))
endingOdometerReading = int(input("Please enter the ending odometer reading: "))
gallonsToFillTank = float(input("Please enter the number of gallons to fill the tank: "))
costPerGallonOfGas = float(input("Please enter the cost per gallon of fuel: "))
numberMilesDrivenPerYear = int(input("Please enter the number of miles driven per year: "))

totalMilesDriven = endingOdometerReading - beginningOdometerReading
averageMilesPerGallon = totalMilesDriven / gallonsToFillTank

costOfGas = gallonsToFillTank * costPerGallonOfGas
fuelCostPerMile = costOfGas/totalMilesDriven

annualCostOfFuel = (numberMilesDrivenPerYear/averageMilesPerGallon) * costPerGallonOfGas

print("Average Miles Per Gallon:",format(averageMilesPerGallon, "<2.2f"))
print("Fuel Cost Per Mile:", '${:,.2f}'.format(fuelCostPerMile))
print("Annual Cost of Fuel:", '${:,.2f}'.format(annualCostOfFuel))
