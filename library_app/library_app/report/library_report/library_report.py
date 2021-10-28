import frappe
from frappe import _

def execute(filters=None):
  return get_columns(), get_data(filters)

def get_data(filters):
    data = frappe.db.sql("""SELECT from_date, to_date, book_name, count(*) as number_of_transactions FROM tabTransactions GROUP BY book_name ORDER BY number_of_transactions DESC;""")
    return data

def get_columns():
    return [
    "From Date:Date",
    "To Date:Date",
    "Book Name:Data",
    "Number Of Transactions:Int"
  ]