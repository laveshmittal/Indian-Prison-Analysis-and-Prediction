from django.shortcuts import render,redirect
from .models import *

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import array
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request,'dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def onlystate(request):
    return render(request,"onlystate.html")

def predictfunc(request):
    return render(request,"predictfunc.html")


def onlyyear(request):
    return render(request,"onlyyear.html")


def app1homepage(request):

    return render(request,'app1homepage.html')

def statecount (request):
    return render(request,'func1.html')

def dashboard(request):
    return render(request,'dashboard.html')

def educationcount(request):
    return render(request,'educationcountfunc.html')

def func1(request):
    ageobject = agegroup.objects.all()

    state = []
    year = []
    category = []
    for item in ageobject:
        state.append(item.state_name)
        year.append(item.year)
        category.append(item.category)
    state_dict = {i: state.count(i) for i in state}
    state_name = list(state_dict.keys())
    print(state_name)
    year_dict = {i: year.count(i) for i in year}
    year_name = list(year_dict.keys())
    category_dict = {i: category.count(i) for i in category}
    category_name = list(category_dict.keys())
    print(category_name)
    dict1 ={}
    l1 = list(range(20))
    for i in range(20):
        l1[i] = 0


    statevar = request.GET.get("statelist", "")
    for item in ageobject:
        if(item.state_name == statevar):
            a = (item.year % 2000)
            l1[a] += (item.age_16_18 + item.age_18_30 + item.age_30_50 + item.age_50_above)
    l1 = l1[1:14]
    print(l1)
    passdict = {'year_name':year_name,'state':statevar,'year_count':l1}
    return render(request,'statecountgraph.html',passdict)

def educationcountfunc(request):
    eduobject = education.objects.all()

    state = []
    year = []
    category = []
    for item in eduobject:
        state.append(item.state_name)
        year.append(item.year)
        category.append(item.education)
    state_dict = {i: state.count(i) for i in state}
    state_name = list(state_dict.keys())
    print(state_name)
    year_dict = {i: year.count(i) for i in year}
    year_name = list(year_dict.keys())
    category_dict = {i: category.count(i) for i in category}
    category_name = list(category_dict.keys())
    print(category_name)
    dict1 ={}

    # Below Class X', 'Class X and above but below graduate', 'Graduate', 'Holding technical degree/diploma etc', 'Illiterate', 'Post-Graduate'
    l1 = list(range(20))
    l2 = list(range(20))
    l3 = list(range(20))
    l4 = list(range(20))
    l5 = list(range(20))
    l6 = list(range(20))

    for i in range(20):
        l1[i] = 0
        l2[i] = 0
        l3[i] = 0
        l4[i] = 0
        l5[i] = 0
        l6[i] = 0


    statevar = request.GET.get("statelist", "")
    for item in eduobject:
        if(item.state_name == statevar):
            a = (item.year % 2000)
            if(item.education == 'Below Class X'):
                l1[a] += item.count
            elif(item.education == 'Class X and above but below graduate'):
                l2[a] += item.count
            elif (item.education == 'Graduate'):
                l3[a] += item.count
            elif (item.education == 'Holding technical degree/diploma etc'):
                l4[a] += item.count
            elif (item.education == 'Illiterate'):
                l5[a] += item.count
            elif (item.education == 'Post-Graduate'):
                l6[a] += item.count




    l1 = l1[1:14]
    l2 = l2[1:14]
    l3 = l3[1:14]
    l4 = l4[1:14]
    l5 = l5[1:14]
    l6 = l6[1:14]
    labels = ['Below Class X','Class X and above but below graduate','Graduate','Holding technical degree/diploma etc','Illiterate','Post-Graduate']
    passdict = {'year_name':year_name,'state':statevar,'l1':l1,'l2':l2,'l3':l3,'l4':l4,'l5':l5,'l6':l6,'labels':labels}
    return render(request,'educationcountgraph.html',passdict)

def escapescount(request):
    return render(request,'escapescountfunc.html')

def escapescountfunc(request):
    escapesobject = escapes.objects.all()

    state = []
    year = []
    detail = []
    for item in escapesobject:
        state.append(item.state_name)
        year.append(item.year)
        detail.append(item.detail)
    state_dict = {i: state.count(i) for i in state}
    state_name = list(state_dict.keys())
    print(state_name)
    year_dict = {i: year.count(i) for i in year}
    year_name = list(year_dict.keys())
    detail_dict = {i: detail.count(i) for i in detail}
    detail_name = list(detail_dict.keys())
    print(detail_name)
    dict1 = {}
    #
    # ['Escapees from Inside Prison', 'Escapees from Outside Prison', 'Escapees from Police Custody', 'Re-arrested escapees']
    l1 = list(range(20))
    l2 = list(range(20))
    l3 = list(range(20))
    l4 = list(range(20))
    for i in range(20):
        l1[i] = 0
        l2[i] = 0
        l3[i] = 0
        l4[i] = 0

    statevar = request.GET.get("statelist", "")
    for item in escapesobject:
        if (item.state_name == statevar):
            a = (item.year % 2000)
            if (item.detail == 'Escapees from Inside Prison'):
                l1[a] += item.total
            elif (item.detail == 'Escapees from Outside Prison'):
                l2[a] += item.total
            elif (item.detail == 'Escapees from Police Custody'):
                l3[a] += item.total
            elif (item.detail == 'Re-arrested escapees'):
                l4[a] += item.total

    l1 = l1[1:14]
    l2 = l2[1:14]
    l3 = l3[1:14]
    l4 = l4[1:14]
    labels = ['Escapees from Inside Prison', 'Escapees from Outside Prison', 'Escapees from Police Custody',
              'Re-arrested escapees']
    passdict = {'year_name': year_name, 'state': statevar, 'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4,
                'labels': labels}
    return render (request,'escapescountgraph.html',passdict)

def sentenceperiod(request):
    return render(request,'sentencefunc.html')

def sentecefunc(request):
    sentenceobject = periodofsentence.objects.all()

    state = []
    year = []
    period = []
    for item in sentenceobject:
        period.append(item.sentence_period)
    # state_dict = {i: state.count(i) for i in state}
    # state_name = list(state_dict.keys())
    # print(state_name)
    # year_dict = {i: year.count(i) for i in year}
    # year_name = list(year_dict.keys())
    period_dict = {i: period.count(i) for i in period}
    period_name = list(period_dict.keys())
    print(period_name)
    # dict1 = {}
    # #
    # # ['age_16_18_years', 'age_18_30_years', 'age_30_50_years', 'age_50_above']
    l1 = list(range(20))
    l2 = list(range(20))
    l3 = list(range(20))
    l4 = list(range(20))
    for i in range(20):
        l1[i] = 0
        l2[i] = 0
        l3[i] = 0
        l4[i] = 0
    # 'Capital Punishment', 'Life Imprisonment', '10-13 Plus years', '7-9 Plus years', '5-6 Plus years', '2-4 Plus years', '1 Less than 2 years', '6 months less than 1 Yr.', '3 - 6 months', 'Less than 3 months', '3 less than 6 months', '10  Less than 3 months']
    statevar = request.GET.get("statelist", "")
    yearvar = request.GET.get("yearlist","")
    yearvar = int(yearvar)
    a = 0
    # print(statevar,yearvar)
    for item in sentenceobject:
        if(item.state_name == statevar):

            if (item.sentence_period == 'Capital Punishment'):
                a = 1
            elif (item.sentence_period == 'Life Imprisonment'):
                a = 2
            elif (item.sentence_period == '10-13 Plus years'):
                a = 3
            elif (item.sentence_period == '7-9 Plus years'):
                a = 4
            elif (item.sentence_period == '5-6 Plus years'):
                a = 5
            elif (item.sentence_period == '2-4 Plus years'):
                a = 6
            elif (item.sentence_period == '1 Less than 2 years'):
                a = 7
            elif (item.sentence_period == '6 months less than 1 Yr'):
                a = 8
            elif (item.sentence_period == '3 - 6 months'):
                a = 9
            elif (item.sentence_period == 'Less than 3 months'):
                a = 10
            elif (item.sentence_period == '3 less than 6 months'):
                a = 11
            elif (item.sentence_period == '10  Less than 3 months'):
                a = 12

            l1[a] += item.age_16_18_years

            l2[a] += item.age_18_30_years

            l3[a] += item.age_30_50_years

            l4[a] += item.age_50_above

    l1 = l1[1:14]
    l2 = l2[1:14]
    l3 = l3[1:14]
    l4 = l4[1:14]

    label = ["Capital Punishment", "Life Imprisonment", "10-13 Plus years", "7-9 Plus years", "5-6 Plus years",
             "2-4 Plus years", "1 Less than 2 years", "6 months less than 1 Yr", "3 - 6 months", "Less than 3 months",
             "3 less than 6 months", "10  Less than 3 months"]

    passdict = {'year': yearvar, 'state': statevar, 'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4,'label':label}
    return render(request, 'sentencegraph.html',passdict)




def predictcount(request):
    ageobject = agegroup.objects.all()

    state = []
    year = []
    category = []
    for item in ageobject:
        state.append(item.state_name)
        year.append(item.year)
        category.append(item.category)
    state_dict = {i: state.count(i) for i in state}
    state_name = list(state_dict.keys())
    print(state_name)
    year_dict = {i: year.count(i) for i in year}
    year_name = list(year_dict.keys())
    category_dict = {i: category.count(i) for i in category}
    category_name = list(category_dict.keys())
    print(category_name)
    dict1 ={}
    l1 = list(range(20))
    for i in range(20):
        l1[i] = 0


    statevar = request.GET.get("statelist", "")
    yearvar = request.GET.get("yearlist","")
    yearvar = int(yearvar)
    passyearvar=yearvar
    yearvar = [yearvar]
    for item in ageobject:
        if(item.state_name == statevar):
            a = (item.year % 2000)
            l1[a] += (item.age_16_18 + item.age_18_30 + item.age_30_50 + item.age_50_above)
    l1 = l1[1:14]
    print(l1)
    X= [(i,i**2) for i in year_name]
    y=l1
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    print(y)
    xpredict = [(i, i ** 2) for i in yearvar]
    y_predicted = lm.predict(xpredict)
    print(y_predicted)
    y_predicted = int(y_predicted)
    passdict = {'year_name':passyearvar,'state':statevar,'predict_value':y_predicted}

    return render(request,'predict.html',passdict)
