import os
from dotenv import load_dotenv

from flat import Bill, Flatmate
from reports import PdfReport, Fileshare

# getting the values from the user
input_amount = float(input("Enter the bill amount: "))
input_period = input("Enter the bill month: ")
input_flatmate1 = input("Enter the name of flatmate 1: ")
input_flatmate1_days = float(input(f"Enter the number of days {input_flatmate1} stayed in house: "))
input_flatmate2 = input("Enter the name of flatmate 2: ")
input_flatmate2_days = float(input(f"Enter the number of days {input_flatmate2} stayed in house: "))

# creation of objects
the_bill = Bill(amount=input_amount, period=input_period)
guest_1 = Flatmate(name=input_flatmate1, days_in_house=input_flatmate1_days)
guest_2 = Flatmate(name=input_flatmate2, days_in_house=input_flatmate2_days)

# calling the pays() method of the class Flatmate
print(f"{guest_1.name} pays: {guest_1.pays(bill=the_bill, flatmate2=guest_2)}")
print(f"{guest_2.name} pays: {guest_2.pays(bill=the_bill, flatmate2=guest_1)}")

# creating the pdf class object and calling its generate() method
pdf_generator = PdfReport(filename=f"{the_bill.period.replace(' ', '_')}.pdf")
pdf_generator.generate(flatmate1=guest_1, flatmate2=guest_2, bill=the_bill)

# using a .env file for aws_access_key and aws_secret_key and loading them
# creating the object for the file sharing class and generating the link to the pdf
load_dotenv(r'C:\Python_Projects\App-2-Flatmates-Bill\dot.env')
file_path = os.path.join("files", f"{the_bill.period.replace(' ', '_')}.pdf")
fs = Fileshare(aws_access_key=os.getenv('AWS_ACCESS_KEY_ID'),
               aws_secret_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
               bucket_name='joab-file-share-bucket',
               file_path=file_path)

link = fs.share()
print(f"Public link: {link}")
