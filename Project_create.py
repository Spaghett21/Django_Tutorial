# Step 1: Create a virtual environment for project isolation
# python -m venv venv

# Step 2: Activate the virtual environment
# On Windows (PowerShell):
# venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# If activation fails, check the execution policy (Windows-specific)
# This command shows the current execution policy
# Get-ExecutionPolicy

# If the policy is too restrictive, allow running scripts in the current user scope
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Try activating the virtual environment again
# venv\Scripts\activate

# Step 3: Install Django in the virtual environment
# python -m pip install Django

# Step 4: Create a new Django project named 'studentsapp' in the current directory
# django-admin startproject studentsapp .

# Step 5: Run the development server to verify installation
 #python manage.py runserver

# Step 6: Install Django REST framework for API development
# pip install djangorestframework

# Step 7: Register the 'rest_framework' in Django settings
# Open settings.py and add 'rest_framework' to the INSTALLED_APPS list:
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     ...
# ]

# Step 8: Freeze dependencies into a requirements file for easy sharing
# pip freeze > requirements.txt

# Step 9: Create a new Django app named 'students'
# django-admin startapp students