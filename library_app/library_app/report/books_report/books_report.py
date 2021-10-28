import frappe
from frappe import _

def execute(filters=None):
  return get_columns(), get_data(filters)

def get_data(filters):
    data = frappe.db.sql("""SELECT title, author, status, publisher, isbn, book_stock, number_of_copies FROM tabBooks;""")
    return data

def get_columns():
    return [
    "Title:Data",
    "Author:Data",
    "Status:Data",
    "Publisher:Data",
    "ISBN:Data",
    "Number Of Copies:Data",
    "Available Copies:Data"
  ]