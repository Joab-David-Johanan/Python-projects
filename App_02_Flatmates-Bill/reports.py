import webbrowser
import os

import boto3
from botocore.exceptions import NoCredentialsError
from fpdf import FPDF


class PdfReport:
    """
    This class creates a pdf file that contains data about bill amount, period, flatmate names,
    the amount each flatmate has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add image
        pdf.image(r"C:\Python_Projects\App-2-Flatmates-Bill\files\house.png", w=50, h=50)

        # create a title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates bill", border=0, align="C", ln=1)

        # add period of the bill
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Total Amount:", border=0)
        pdf.cell(w=150, h=40, txt=str(bill.amount), border=0, ln=1)

        # add flatmate1 and their amount
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        # add flatmate2 and their amount
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0)

        # change directory to access the generated pdf
        os.chdir(r"C:\Python_Projects\App-2-Flatmates-Bill\files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

        # pdf.output(os.path.join("files", self.filename))
        # webbrowser.open(os.path.join("files", self.filename))


class Fileshare:
    """
        This class is used to upload files to the cloud and share a link to view the uploaded files.
    """

    def __init__(self, aws_access_key, aws_secret_key, bucket_name, file_path):
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket_name = bucket_name
        self.file_path = file_path

    def share(self):
        s3 = boto3.client('s3',
                          aws_access_key_id=self.aws_access_key,
                          aws_secret_access_key=self.aws_secret_key)
        try:
            file_name = self.file_path.split('/')[-1]

            # Upload the file
            s3.upload_file(self.file_path, self.bucket_name, file_name)

            # Now generate pre-signed URL
            url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': file_name},
                ExpiresIn=3600
            )

            return url

        except FileNotFoundError:
            print("The file was not found")
        except NoCredentialsError:
            print("Credentials not available")
