import csv
import datetime

import numpy as np
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import string
import os

class RecordList:
    recordList = []

    def __init__(self):
        self.recordList = self.readXLS()

    def readXLS(self):
        workpath = os.path.dirname(os.path.abspath(__file__))    
        with open(os.path.join(workpath, 'pko17.csv'), newline = "\n") as csvfile:
            reader = csv.reader(csvfile, delimiter = ",")
            next(reader, None)
            self.recordList = []
            for row in reader:
                self.recordList.append(Record(row[0], round(float(row[3]),2), row[0]))
            return self.recordList
    
    def findByYear(self, date):
        recordsInYear = []
        for r in self.recordList:
            if r.date.year == date.year :
                recordsInYear.append(r)
        return recordsInYear
    
    def findByMonth(self, date):
        recordsInMonth = []
        for r in self.recordList:
            if r.date.month == date.month and r.date.year == date.year :
                recordsInMonth.append(r)
        return recordsInMonth
    
    def findByDay(self, date):
        recordsInDay = []
        for r in self.recordList:
            if r.date == date:
                recordsInDay.append(r)
        return recordsInDay

    def sumExpensesInDay(self, date):
        records = self.findByDay(date)
        sum = 0.0
        for row in records:
            if row.amount < 0:
                sum += row.amount
        return sum
    
    def sumExpensesInMonth(self, var):
        records = self.findByMonth(var)
        sum = 0.0
        for row in records:
            if row.amount < 0:
                sum += row.amount
        return sum
    
    def sumIncomeInMonth(self, var):
        records = self.findByMonth(var)
        sum = 0.0
        for row in records:
            if row.amount > 0:
                sum += row.amount
        return sum

    def mergedExpensesByMonth(self, date):
        recordsInMonth = []
        sum = 0.0
        for i in range(1,31):
            newdate = date.replace(day = i)
            sum = self.sumExpensesInDay(newdate)
            recordsInMonth.append(sum)
        return recordsInMonth

    def mergedExpensesByYear(self, date):
        recordsInYear = []
        sum = 0.0
        for i in range(0,11):
            newdate = date.replace(month = i+1)
            sum = self.sumExpensesInMonth(newdate)
            recordsInYear.append(sum)
        return recordsInYear

class Record:
    date = datetime.MINYEAR
    amount = 0.0
    description = ""
    def __init__(self, d, a, desc):
        self.date = datetime.datetime.strptime(d, '%Y-%m-%d')
        self.amount = a
        self.description = desc
    
    def __str__(self):
        return str(self.date, self.amount, self.description)

    def __repr__(self):
        delimiter = " "
        seq = (str(self.date.month),str(self.date.year), str(self.amount), str(self.description))
        return delimiter.join(seq)

rlist = RecordList()
# plotExpensesByMonth()
# plotExpensesInYear()

