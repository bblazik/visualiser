from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from . import sample
import logging

from jchart import Chart
from jchart.config import Axes, DataSet

from .engine.core import RecordList
from datetime import datetime
from dateutil.relativedelta import relativedelta

import sys

logger = logging.getLogger(__name__)

class LineChart(Chart):
    chart_type = 'line'
    resposive = True
    rrlist = []

    scales = {
        'xAxes': [Axes(type='linear', position='bottom')],
    }
    def __init__(self, records): # there must be initialization list with multiple arguments
        self.rrlist = records
        super(LineChart,self).__init__()

    def get_datasets(self, **kwargs):
        data = [
            DataSet(label= "Expenses",
                backgroundColor = 'rgba(230,71,89, 0.7)',
                data= [{'x': record[0], 'y': record[1]} for record in self.rrlist[0]]
            ),
            DataSet(label= "Income",
                backgroundColor = 'rgba(27,	201, 142, 0.7)',
                data= [{'x': record[0], 'y': record[1]} for record in self.rrlist[1]]
            ),
            DataSet(label= "Balance",
                backgroundColor = 'rgba(27,	201, 142, 0.7)',
                data= [{'x': record[0], 'y': record[1]} for record in self.rrlist[1]]
            )

        ]
        return data

targetDate = datetime.now().strftime('%m %d %Y')

def monthlyReport(request):
    return render(request, 'line_chart.html', {
        'line_chart': LineChart(prepereMonthlyData()),
        'targetDate': targetDate
    })

def yearlyReport(request):
    return render(request, 'line_chart.html', {
        'line_chart': LineChart(prepereYearlyData()),
    })

def prepereYearlyData(data = datetime.strptime('2017-09-15', '%Y-%m-%d')):
    rlist = RecordList().mergedExpensesByYear(data)
    ilist = RecordList().mergedIncomeByYear(data)

    rrlist = [[], []]
    for i in range(0, len(rlist)):
        rrlist[0].append( (i+1, rlist[i]))
    for i in range(0, len(ilist)):
        rrlist[1].append( (i+1, ilist[i]))
    return rrlist

def prepereMonthlyData(data= datetime.strptime('2017-09-15', '%Y-%m-%d')):    
    rlist = RecordList().mergedExpensesByMonth(data)
    ilist = RecordList().mergedIncomeByMonth(data)

    rrlist = [[], []]
    for i in range(0, len(rlist)):
        rrlist[0].append( (i+1, rlist[i]))
    for i in range(0, len(ilist)):
        rrlist[1].append( (i+1, ilist[i]))
    return rrlist

def nextMonth(request):
    if request.method == 'POST':
        targetDate = datetime.strptime(request.POST.get('date'), '%m %d %Y' )        
        targetDate = targetDate + relativedelta(months=1)
        return renderPageData(targetDate, request)
    
def previousMonth(request):
    if request.method == 'POST':
        targetDate = datetime.strptime(request.POST.get('date'), '%m %d %Y' )
        targetDate = targetDate - relativedelta(months=1)
        return renderPageData(targetDate, request)

def pickedDate(request):    
    if request.method == 'POST':
        targetDate = datetime.strptime(request.POST.get('date'), '%m %d %Y' )
        return renderPageData(targetDate, request)
    
def renderPageData(targetDate, request):
    expenses = RecordList().sumExpensesInMonth(targetDate)
    income = RecordList().sumIncomeInMonth(targetDate);

    return render(request, 'line_chart.html', {
        'line_chart': LineChart(prepereMonthlyData(targetDate)),
        'targetDate': targetDate.strftime('%m %d %Y'),
        'expenses': expenses,
        'income': income,
    })

def visualiseDate(request):
    recordList = {'recordList' : RecordList().recordList}
    return render(request, 'visualiseData.html', recordList)


