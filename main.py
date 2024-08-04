import pdfkit

url = input("Your link: \n")
html_file = input("enter the path: \n")
file_name = input("Enter your file name: \n")

pdfkit.from_url(url, f"{file_name}.pdf")
pdfkit.from_file(html_file, f"{file_name}.pdf")