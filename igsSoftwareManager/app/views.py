from django.shortcuts import render
from app.models import Employee, Department
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import serializers, status
from app.serializers import EmployeeSerializer, DepartmentSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List of all Employees': '/employee/',
        'List of all Departments': '/department/',
        'Add Employee': '/employee/add',
        'Add Department': '/department/add',
        'Get one Employee by id': '/employee/<id>',
        'Get one Department by id': '/department/<id>',
        'Update Employee': '/employee/update/<id>',
        'Update Department': '/department/update/<id>',
        'Delete an employee': '/employee/delete/<id>',
        'Delete a department': '/department/delete/<id>'
    }

    return Response(api_urls)


# Employee CRUD
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_employee(request):
    employee = EmployeeSerializer(data=request.data)

    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This employee already exist.")

    if employee.is_valid():
        employee.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(employee.errors)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_employee_by_id(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except:
        raise serializers.ValidationError("This employee doesn't exist.")


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_all_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)

    if serializer:
        return Response(serializer.data)
    else:
        raise serializers.ValidationError("No registered employee.")


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except:
        raise serializers.ValidationError("This employee doesn't exist.")

    if employee:
        data = EmployeeSerializer(instance=employee, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except:
        raise serializers.ValidationError("This employee doesn't exist.")

    if employee:
        employee.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# Department CRUD
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_department(request):
    department = DepartmentSerializer(data=request.data)

    if Department.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This department already exist.")

    if department.is_valid():
        department.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(department.errors)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_department_by_id(request, id):
    try:
        department = Department.objects.get(id=id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    except:
        raise serializers.ValidationError("This department doesn't exist.")


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_all_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)

    if serializer:
        return Response(serializer.data)
    else:
        raise serializers.ValidationError("No registered departments.")


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_department(request, id):
    try:
        department = Department.objects.get(id=id)
    except:
        raise serializers.ValidationError("This department doesn't exist.")

    if department:
        data = DepartmentSerializer(instance=department, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_department(request, id):
    try:
        department = Department.objects.get(id=id)
    except:
        raise serializers.ValidationError("This department doesn't exist.")

    if department:
        department.delete()
        return Response(status.HTTP_204_NO_CONTENT)


def list_view(request):
    template = 'app/index.html'
    output_data = list(Employee.objects.values())

    for entry in output_data:
        department_id = entry['department_id']
        department_name = Department.objects.get(id=department_id).name
        entry['department_name'] = department_name

    context = {
        "employees": output_data
    }

    return render(request, template, context)
