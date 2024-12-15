from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def homepage_function(request):
    isActive = True

    if request.method == 'POST':
        data = request.POST.get('InputField01')
        print(data)
        if data is None:
            isActive = False
        else:
            isActive = True
    
    # Dynamic Content
    date = datetime.now()
    # print(date)

    name = 'Akshay Yewle'
    list_of_programs = ['Check Even of Odd Number','Check Prime Number',
                        'Write all prime numbers from 1 to 100','WAP to print pascals triangle',]

    student_data = {'student_name': "Akshay",'student_college': "XYZ University",
                    'student_city': "New Delhi",}

    data = {'date': date,'isActive': isActive,'name': name,
            'list_of_programs': list_of_programs,'student': student_data}

    # return HttpResponse("This is Home Page")
    return render(request, 'home.html',data)

def test_function(request):
    print('test function is called from view')
    # return HttpResponse("Hello World!" + str(datetime.now()))
    return render(request, 'test.html')

def about_function(request):
    print('about function is called from view')
    # return HttpResponse("This is About Page" + str(datetime.now()))
    return render(request, 'about.html',{})

def services_function(request):
    print('services page is called from view')
    # return HttpResponse("This is Services Page" + str(datetime.now()))
    return render(request,'services.html',{})