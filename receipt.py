#!/usr/bin/python
#File Name: receipt.py

#Imports
from datetime import datetime
import time

#Header
print("         Affordable Daily Needs        ")
print("This program will prompt for 10 items. ")
print("Enter quantity of each item purchased  ")

#Prompts
Bread = int(input("How many loaves of Bread ($1.50 each): "))
Milk = int(input("How many gallons of Milk ($2.25 each): "))
Chips = int(input("How many bags of Chips ($3.60 each) : "))
Potatoes = float(input("How many pounds of Potatoes ($0.99/lb) : "))
Bananas = float(input("How many pounds of Bananas ($0.36/lb) : "))
Beef = float(input("How many pounds of Beef ($3.89/lb) : "))
Tomatoes = float(input("How many pounds of Tomatoes ($0.89/lb) : "))
Apples = float(input("How many pounds of Apples ($0.69/lb) : "))
Batteries = int(input("How many 2-pack AA batteries ($2.29 each): "))
Vitamins = int(input("How many Vitamin bottles ($4.59 each): "))

#Prices
priceBread=1.50
priceMilk=2.25
priceChips=3.60
pricePotatoes=0.99
priceBananas=0.36
priceBeef=3.89
priceTomatoes=0.89
priceApples=0.69
priceBatteries=2.29
priceVitamins=4.59

#Costs
costBread=priceBread*Bread
costMilk=priceMilk*Milk
costChips=priceChips*Chips
costPotatoes=pricePotatoes*Potatoes
costBananas=priceBananas*Bananas
costBeef=priceBeef*Beef
costTomatoes=priceTomatoes*Tomatoes
costApples=priceApples*Apples
costBatteries=priceBatteries*Batteries
costVitamins=priceVitamins*Vitamins

#Sub Total
subTotal = costBread + costMilk + costChips + costPotatoes + costBananas + costBeef + costTomatoes + costApples + costBatteries + costVitamins

#Taxes
taxBatteries = costBatteries * 0.0825
taxVitamins = costVitamins * 0.0825
totalTax = taxBatteries + taxVitamins

#Total Cost
totalCost = subTotal + totalTax

#Receipt
print("                                       ")
print("=======================================")
print("         Affordable Daily Needs        ")
print("          2300 N. Loop 1604 E          ")
print("          San Antonio TX 78258         ")
print("---------------------------------------")
print("Item          Qty   price/unit   cost  ")
print("---------------------------------------")
print("%-10s %6.1f %9.2f %9.2f" % ("Bread", float(Bread), float(priceBread), float(costBread)))
print("%-10s %6.1f %9.2f %9.2f" % ("Milk", float(Milk), float(priceMilk), float(costMilk)))
print("%-10s %6.1f %9.2f %9.2f" % ("Chips", float(Chips), float(priceChips), float(costChips)))
print("%-10s %6.1f %9.2f %9.2f" % ("Potatoes", float(Potatoes), float(pricePotatoes), float(costPotatoes)))
print("%-10s %6.1f %9.2f %9.2f" % ("Bananas", float(Bananas), float(priceBananas), float(costBananas)))
print("%-10s %6.1f %9.2f %9.2f" % ("Beef", float(Beef), float(priceBeef), float(costBeef)))
print("%-10s %6.1f %9.2f %9.2f" % ("Tomatoes", float(Tomatoes), float(priceTomatoes), float(costTomatoes)))
print("%-10s %6.1f %9.2f %9.2f" % ("Apples", float(Apples), float(priceApples), float(costApples)))
print("%-10s %6.1f %9.2f %9.2f" % ("Batteries", float(Batteries), float(priceBatteries), float(costBatteries)))
print("%-10s %6.1f %9.2f %9.2f" % ("Vitamins", float(Vitamins), float(priceVitamins), float(costVitamins)))
print(".......................................")
print("%-10s %26.2f" % ("Sub Total", float(subTotal)))
print("%-10s %25.2f" % ("Tax @ 8.25%", float(totalTax)))
print("---------------------------------------")
print("%-10s %26.2f" % ("TOTAL", float(totalCost)))
print("=======================================")
print("Sales Clerk: Luis Navarro              ")
print("Date: %s" % (time.strftime('%m/%d/%Y %H:%M:%S') ))
