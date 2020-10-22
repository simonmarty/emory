#!/usr/bin/env python3

import pandas as pd
import numpy as np

def main():
	quests = pd.read_csv("CS470_570-S20 Multiple Choice Question Writing - Midterm 2 (Responses) - Form Responses 1.csv")
	while(len(quests.index) != 0):
		randquest = quests.sample()
		print(randquest['Question'].values[0])
		print(f"A: {randquest['A'].values[0]}")
		print(f"B: {randquest['B'].values[0]}")
		print(f"C: {randquest['C'].values[0]}")
		print(f"D: {randquest['D'].values[0]}")
		print(f"E: {randquest['E'].values[0]}")
		input()
		print(f"Correct Answer: {randquest['Correct Answer'].values[0]}")
		print(f"References: {randquest['References'].values[0]}")
		quests = quests.drop(randquest.index)
	print("You studied all of the questions!")
if __name__ == "__main__":
	main()
