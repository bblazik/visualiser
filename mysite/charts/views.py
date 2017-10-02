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

import sys

logger = logging.getLogger(__name__)

class LineChart(Chart):
    chart_type = 'line'
    resposive = True
    rrlist = []

    scales = {
        'xAxes': [Axes(type='linear', position='bottom')],
    }
    def __init__(self, records):
        self.rrlist = records
        super(LineChart,self).__init__()

    def get_datasets(self, **kwargs):
        data = [
            DataSet(label= "My Dataset",
                backgroundColor = 'rgba(255, 99, 132, 0.7)',
                data= [{'x': record[0], 'y': record[1]} for record in self.rrlist]
            ),
            DataSet(label= "My Dataset1",
                backgroundColor = 'rgba(255, 99, 0, 0.7)',
                data= [{'x': record[0], 'y': record[1]} for record in self.rrlist]
            )
        ]
        return data


def index(request):
    sum = sample.sumTwo()
    context = {'sum': sum}
    return render(request, 'index.html', context)

def monthlyReport(request):
    return render(request, 'line_chart.html', {
        'line_chart': LineChart(prepereMonthlyData()),
    })

def yearlyReport(request):
    return render(request, 'line_chart.html', {
        'line_chart': LineChart(prepereYearlyData()),
    })

def prepereYearlyData():
    exampleData = datetime.strptime('2017-09-15', '%Y-%m-%d')
    rlist = RecordList().mergedExpensesByYear(exampleData)
    rrlist = []
    for i in range(0, len(rlist)):
        rrlist.append( (i+1, rlist[i]))
    return rrlist

def prepereMonthlyData():
    exampleData = datetime.strptime('2017-06-11', '%Y-%m-%d')
    rlist = RecordList().mergedExpensesByMonth(exampleData)
    rrlist = []
    for i in range(0, len(rlist)):
        rrlist.append( (i+1, rlist[i]))
    return rrlist

def visualiseData(request):
    recordList = {'recordList' : RecordList().recordList}
    return render(request, 'visualiseData.html', recordList)
