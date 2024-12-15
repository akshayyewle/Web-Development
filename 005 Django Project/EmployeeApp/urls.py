from django.urls import re_path as url
from EmployeeApp import views

urlpatterns = [
    url(r'^department$',views.DepartmentsAPI),
    url(r'^department/([0-9]+)',views.DepartmentsAPI),

    url(r'^employees$',views.EmployeesAPI),
    url(r'^employees/([0-9]+)',views.EmployeesAPI)
]