from django.db import transaction
from app1.models import Employee
import threading

def create_employee1():
    print("Saving Employee instance...")
    employee = Employee.objects.create(name="Rahul Dahiya")
    print("Employee instance saved.")
create_employee1()


def create_employee2():
    print(f"Main function is running in thread: {threading.current_thread().name}")
    employee = Employee.objects.create(name="AccuKnox")
    print("Employee instance saved.")
create_employee2()


def create_employee_with_error():
    try:
        with transaction.atomic():
            # Create an Employee instance
            employee = Employee.objects.create(name="John Doe")
            print(f"Employee {employee.name} created with status '{employee.status}'")
            
            # Signal will trigger and change status to 'Processed'
            
            # Raise an intentional error to trigger rollback
            raise Exception("Intentional error to test rollback")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Check if the employee was actually saved (it shouldn't be due to rollback)
    employee_exists = Employee.objects.filter(name="John Doe").exists()
    print(f"Employee exists after rollback? {employee_exists}")
