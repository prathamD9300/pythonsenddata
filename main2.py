# import tkinter as tk
# from tkinter import messagebox
# import pyodbc
# import requests
# import json
# import threading
# import time
# import datetime

# # Fetch attendance data for the past 30 days
# def fetch_attendance_data_from_sql(server_name, database_name, username, password):
#     try:
#         conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;'
#                               f'SERVER={server_name};'
#                               f'DATABASE={database_name};'
#                               f'UID={username};'
#                               f'PWD={password}')
        
#         cursor = conn.cursor()

#         # Fetch attendance data for the past 30 days
#         thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
#         cursor.execute('SELECT * FROM AttendanceLogs WHERE AttendanceDate >= ?', thirty_days_ago)
        
#         attendance_data = []
#         for row in cursor.fetchall():
#             att = {
#                 "AttendanceLogId": row.AttendanceLogId,
#                 "AttendanceDate": str(row.AttendanceDate),
#                 "EmployeeId": row.EmployeeId,
#                 "InTime": str(row.InTime),
#                 "InDeviceId": row.InDeviceId,
#                 "OutTime": str(row.OutTime),
#                 "OutDeviceId": row.OutDeviceId,
#                 "Duration": row.Duration,
#                 "LateBy": row.LateBy,
#                 "EarlyBy": row.EarlyBy,
#                 "IsOnLeave": row.IsOnLeave,
#                 "LeaveType": row.LeaveType,
#                 "LeaveDuration": row.LeaveDuration,
#                 "WeeklyOff": row.WeeklyOff,
#                 "Holiday": row.Holiday,
#                 "LeaveRemarks": row.LeaveRemarks,
#                 "PunchRecords": row.PunchRecords,
#                 "ShiftId": row.ShiftId,
#                 "Present": row.Present,
#                 "Absent": row.Absent,
#                 "Status": row.Status,
#                 "StatusCode": row.StatusCode,
#                 "P1Status": row.P1Status,
#                 "P2Status": row.P2Status,
#                 "P3Status": row.P3Status,
#                 "IsonSpecialOff": row.IsonSpecialOff,
#                 "SpecialOffType": row.SpecialOffType,
#                 "SpecialOffRemark": row.SpecialOffRemark,
#                 "SpecialOffDuration": row.SpecialOffDuration,
#                 "OverTime": row.OverTime,
#                 "OverTimeE": row.OverTimeE,
#                 "MissedOutPunch": row.MissedOutPunch,
#                 "Remarks": row.Remarks,
#                 "MissedInPunch": row.MissedInPunch,
#                 "C1": row.C1,
#                 "C2": row.C2,
#                 "C3": row.C3,
#                 "C4": row.C4,
#                 "C5": row.C5,
#                 "C6": row.C6,
#                 "C7": row.C7,
#                 "LeaveTypeId": row.LeaveTypeId,
#                 "LossOfHours": row.LossOfHours
#             }
#             attendance_data.append(att)
            
#         conn.close()
#         return attendance_data, None
#     except Exception as e:
#         return None, str(e)

# def send_data_to_api(server_name, database_name, username, password, api_endpoint):
#     try:
#         client_id = 'qispl'
#         attendance_data, error = fetch_attendance_data_from_sql(server_name, database_name, username, password)
#         if error is not None:
#             return error

#         if attendance_data is None:
#             return "No attendance data found."

#         payload = {
#             "clientId": client_id,
#             "employeeData": [],
#             "attendanceData": attendance_data,
#         }
#         payload_json = json.dumps(payload)
#         headers = {'Content-Type': 'application/json'}
#         response = requests.post(url=api_endpoint, json=payload, headers=headers)
#         print(response.text)
#         print(payload_json)
        
#         if response.status_code == 200:
#             return f"Data sent successfully to API at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#         else:
#             return f"Failed to send data to API: {response.text}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Function to start automatic synchronization
# def start_auto_sync(server_name, database_name, username, password, api_endpoint, status_label):
#     while True:
#         status = send_data_to_api(server_name, database_name, username, password, api_endpoint)
#         status_label.config(text=status)
#         time.sleep(60)

# # Function to handle button click event
# def connect_to_database(server_entry, database_entry, uid_entry, password_entry, api_endpoint_entry, status_label):
#     try:
#         server = server_entry.get()
#         database = database_entry.get()
#         uid = uid_entry.get()
#         password = password_entry.get()
#         api_endpoint = api_endpoint_entry.get()

#         if not server or not database or not uid or not password or not api_endpoint:
#             status_label.config(text="Please fill in all fields.")
#             return

#         status = send_data_to_api(server, database, uid, password, api_endpoint)
#         status_label.config(text=status)
#     except Exception as e:
#         status_label.config(text=f"Failed to connect to the database: {e}")

# # Create main window
# root = tk.Tk()
# root.title("Database Synchronization")
# root.geometry("400x400")

# # Font settings
# font = ("Arial", 11)

# # Server label and entry
# server_label = tk.Label(root, text="Server Name:", font=font)
# server_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
# server_entry = tk.Entry(root, font=font, width=30)
# server_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# # Database label and entry
# database_label = tk.Label(root, text="Database Name:", font=font)
# database_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# database_entry = tk.Entry(root, font=font, width=30)
# database_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# # UID label and entry
# uid_label = tk.Label(root, text="UID:", font=font)
# uid_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
# uid_entry = tk.Entry(root, font=font, width=30)
# uid_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# # Password label and entry
# password_label = tk.Label(root, text="Password:", font=font)
# password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
# password_entry = tk.Entry(root, show="*", font=font, width=30)
# password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# # API Endpoint label and entry
# api_endpoint_label = tk.Label(root, text="API Endpoint:", font=font)
# api_endpoint_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
# api_endpoint_entry = tk.Entry(root, font=font, width=30)
# api_endpoint_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# # Status label
# status_label = tk.Label(root, text="", font=font)
# status_label.grid(row=5, column=0, columnspan=2, pady=10)

# # Start Auto Sync button
# start_auto_sync_button = tk.Button(root, text="Start Sync", command=lambda: threading.Thread(target=start_auto_sync, args=(server_entry.get(), database_entry.get(), uid_entry.get(), password_entry.get(), api_endpoint_entry.get(), status_label)).start(), font=font)
# start_auto_sync_button.grid(row=6, column=0, columnspan=2, pady=10)

# # Connect to Database button
# connect_button = tk.Button(root, text="Send Data", command=lambda: connect_to_database(server_entry, database_entry, uid_entry, password_entry, api_endpoint_entry, status_label), font=font)
# connect_button.grid(row=7, column=0, columnspan=2, pady=10)

# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import pyodbc
import requests
import json
import threading
import time
import datetime

# Fetch attendance data for the past 30 days
def fetch_attendance_data_from_sql(server_name, database_name, username, password):
    try:
        conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;'
                              f'SERVER={server_name};'
                              f'DATABASE={database_name};'
                              f'UID={username};'
                              f'PWD={password}')
        
        cursor = conn.cursor()

        # Fetch attendance data for the past 30 days
        thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
        cursor.execute('SELECT * FROM AttendanceLogs WHERE AttendanceDate >= ?', thirty_days_ago)
        
        attendance_data = []
        for row in cursor.fetchall():
            att = {
                "AttendanceLogId": row.AttendanceLogId,
                "AttendanceDate": str(row.AttendanceDate),
                "EmployeeId": row.EmployeeId,
                "InTime": str(row.InTime),
                "InDeviceId": row.InDeviceId,
                "OutTime": str(row.OutTime),
                "OutDeviceId": row.OutDeviceId,
                "Duration": row.Duration,
                "LateBy": row.LateBy,
                "EarlyBy": row.EarlyBy,
                "IsOnLeave": row.IsOnLeave,
                "LeaveType": row.LeaveType,
                "LeaveDuration": row.LeaveDuration,
                "WeeklyOff": row.WeeklyOff,
                "Holiday": row.Holiday,
                "LeaveRemarks": row.LeaveRemarks,
                "PunchRecords": row.PunchRecords,
                "ShiftId": row.ShiftId,
                "Present": row.Present,
                "Absent": row.Absent,
                "Status": row.Status,
                "StatusCode": row.StatusCode,
                "P1Status": row.P1Status,
                "P2Status": row.P2Status,
                "P3Status": row.P3Status,
                "IsonSpecialOff": row.IsonSpecialOff,
                "SpecialOffType": row.SpecialOffType,
                "SpecialOffRemark": row.SpecialOffRemark,
                "SpecialOffDuration": row.SpecialOffDuration,
                "OverTime": row.OverTime,
                "OverTimeE": row.OverTimeE,
                "MissedOutPunch": row.MissedOutPunch,
                "Remarks": row.Remarks,
                "MissedInPunch": row.MissedInPunch,
                "C1": row.C1,
                "C2": row.C2,
                "C3": row.C3,
                "C4": row.C4,
                "C5": row.C5,
                "C6": row.C6,
                "C7": row.C7,
                "LeaveTypeId": row.LeaveTypeId,
                "LossOfHours": row.LossOfHours
            }
            attendance_data.append(att)
            
        conn.close()
        return attendance_data, None
    except Exception as e:
        return None, str(e)

# Fetch employee data
def fetch_employee_data_from_sql(server_name, database_name, username, password):
    try:
        conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;'
                              f'SERVER={server_name};'
                              f'DATABASE={database_name};'
                              f'UID={username};'
                              f'PWD={password}')
        
        cursor = conn.cursor()
        
        # Fetch employee data
        cursor.execute('SELECT * FROM Employees')
        
        employee_data = []
        for row in cursor.fetchall():
            emp = {
                "EmployeeId": row.EmployeeId,
                "EmployeeName": row.EmployeeName,
                "EmployeeCode": row.EmployeeCode,
                "StringCode": row.StringCode,
                "NumericCode": row.NumericCode,
                "Gender": row.Gender,
                "CompanyId": row.CompanyId,
                "DepartmentId": row.DepartmentId,
                "Designation": row.Designation,
                "CategoryId": row.CategoryId,
                "DOJ": str(row.DOJ),
                "DOR": str(row.DOR) if row.DOR else None,
                "DOC": str(row.DOC),
                "EmployeeCodeInDevice": row.EmployeeCodeInDevice,
                "EmployeeRFIDNumber": row.EmployeeRFIDNumber,
                "EmploymentType": row.EmploymentType,
                "Status": row.Status,
                "EmployeeDevicePassword": row.EmployeeDevicePassword,
                "EmployeeDeviceGroup": row.EmployeeDeviceGroup,
                "FatherName": row.FatherName,
                "MotherName": row.MotherName,
                "ResidentialAddress": row.ResidentialAddress,
                "PermanentAddress": row.PermanentAddress,
                "ContactNo": row.ContactNo,
                "Email": row.Email,
                "DOB": str(row.DOB),
                "PlaceOfBirth": row.PlaceOfBirth,
                "Nominee1": row.Nominee1,
                "Nominee2": row.Nominee2,
                "Remarks": row.Remarks,
                "RecordStatus": row.RecordStatus,
                "C1": row.C1,
                "C2": row.C2,
                "C3": row.C3,
                "C4": row.C4,
                "C5": row.C5,
                "C6": row.C6,
                "C7": row.C7,
                "Location": row.Location,
                "BloodGroup": row.BloodGroup,
                "WorkPlace": row.WorkPlace,
                "ExtensionNo": row.ExtensionNo,
                "LoginName": row.LoginName,
                "LoginPassword": row.LoginPassword,
                "Grade": row.Grade,
                "Team": row.Team,
                "IsReceiveNotification": row.IsReceiveNotification,
                "HolidayGroup": row.HolidayGroup,
                "ShiftGroupId": row.ShiftGroupId,
                "ShiftRosterId": row.ShiftRosterId,
                "LastModifiedBy": row.LastModifiedBy,
                "AadhaarNumber": row.AadhaarNumber,
                "EmployeePhoto": row.EmployeePhoto,
                "MasterDeviceId": row.MasterDeviceId,
                "BIOPhoto1": row.BIOPhoto1,
                "BIOPhotoPic": row.BIOPhotoPic,
                "DeviceExpiryRule": row.DeviceExpiryRule,
                "DeviceExpiryStartDate": str(row.DeviceExpiryStartDate),
                "DeviceExpiryEndDate": str(row.DeviceExpiryEndDate),
                "DeviceId": row.DeviceId,
                "EnrolledDate": str(row.EnrolledDate),
                "MigrateToOtherCryptography": row.MigrateToOtherCryptography,
                "GeofenceId": row.GeofenceId,
                "MaritalStatus": row.MaritalStatus,
                "Nationality": row.Nationality,
                "PassportNumber": row.PassportNumber,
                "OverallExperience": row.OverallExperience,
                "Qualifications": row.Qualifications,
                "ReferenceDetail": row.ReferenceDetail,
                "EmergencyContact": row.EmergencyContact,
                "SubDepartment": row.SubDepartment,
                "Division": row.Division
            }
            employee_data.append(emp)
            
        conn.close()
        return employee_data, None
    except Exception as e:
        return None, str(e)

def send_data_to_api(server_name, database_name, username, password, api_endpoint):
    try:
        client_id = 'qispl'
        
        attendance_data, attendance_error = fetch_attendance_data_from_sql(server_name, database_name, username, password)
        employee_data, employee_error = fetch_employee_data_from_sql(server_name, database_name, username, password)

        if attendance_error is not None:
            return attendance_error
        if employee_error is not None:
            return employee_error

        if attendance_data is None and employee_data is None:
            return "No data found."

        payload = {
            "clientId": client_id,
            "employeeData": employee_data,
            "attendanceData": attendance_data,
        }
        payload_json = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=api_endpoint, json=payload, headers=headers)
        print(response.text)
        print(payload_json)
        
        if response.status_code == 200:
            return f"Data sent successfully to API at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            return f"Failed to send data to API: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to start automatic synchronization
def start_auto_sync(server_name, database_name, username, password, api_endpoint, status_label):
    while True:
        status = send_data_to_api(server_name, database_name, username, password, api_endpoint)
        status_label.config(text=status)
        time.sleep(60)

# Function to handle button click event
def connect_to_database(server_entry, database_entry, uid_entry, password_entry, api_endpoint_entry, status_label):
    try:
        server = server_entry.get()
        database = database_entry.get()
        uid = uid_entry.get()
        password = password_entry.get()
        api_endpoint = api_endpoint_entry.get()

        if not server or not database or not uid or not password or not api_endpoint:
            status_label.config(text="Please fill in all fields.")
            return

        status = send_data_to_api(server, database, uid, password, api_endpoint)
        status_label.config(text=status)
    except Exception as e:
        status_label.config(text=f"Failed to connect to the database: {e}")

# Create main window
root = tk.Tk()
root.title("Database Synchronization")
root.geometry("400x400")

# Font settings
font = ("Arial", 11)

# Server label and entry
server_label = tk.Label(root, text="Server Name:", font=font)
server_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
server_entry = tk.Entry(root, font=font, width=30)
server_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Database label and entry
database_label = tk.Label(root, text="Database Name:", font=font)
database_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
database_entry = tk.Entry(root, font=font, width=30)
database_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# UID label and entry
uid_label = tk.Label(root, text="UID:", font=font)
uid_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
uid_entry = tk.Entry(root, font=font, width=30)
uid_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Password label and entry
password_label = tk.Label(root, text="Password:", font=font)
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*", font=font, width=30)
password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# API Endpoint label and entry
api_endpoint_label = tk.Label(root, text="API Endpoint:", font=font)
api_endpoint_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
api_endpoint_entry = tk.Entry(root, font=font, width=30)
api_endpoint_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Status label
status_label = tk.Label(root, text="", font=font)
status_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start Auto Sync button
start_auto_sync_button = tk.Button(root, text="Start Sync", command=lambda: threading.Thread(target=start_auto_sync, args=(server_entry.get(), database_entry.get(), uid_entry.get(), password_entry.get(), api_endpoint_entry.get(), status_label)).start(), font=font)
start_auto_sync_button.grid(row=6, column=0, columnspan=2, pady=10)

# Connect to Database button
connect_button = tk.Button(root, text="Send Data", command=lambda: connect_to_database(server_entry, database_entry, uid_entry, password_entry, api_endpoint_entry, status_label), font=font)
connect_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
