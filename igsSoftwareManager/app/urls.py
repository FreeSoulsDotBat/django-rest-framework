from django.urls import path
from . import views

urlpatterns = [
    # API overview
    path('', views.ApiOverview, name='home'),
    # Employee endpoints
    path('employee/', views.get_all_employees, name='get-all-employees'),
    path('employee/add', views.add_employee, name='add-employee'),
    path('employee/<int:id>', views.get_employee_by_id, name='get-employee'),
    path('employee/update/<int:id>', views.update_employee, name='update-employee'),
    path('employee/delete/<int:id>', views.delete_employee, name='delete-employee'),
    # Department endpoints
    path('department/', views.get_all_departments, name='get-all-departments'),
    path('department/add', views.add_department, name='add-department'),
    path('department/<int:id>', views.get_department_by_id, name='get-department'),
    path('department/update/<int:id>',
         views.update_department, name='update-department'),
    path('department/delete/<int:id>',
         views.delete_department, name='delete-department'),
]
