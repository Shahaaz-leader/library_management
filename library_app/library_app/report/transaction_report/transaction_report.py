import frappe
from frappe import _

def execute(filters=None):
  return get_columns(), get_data(filters)

def get_data(filters):
    data = frappe.db.sql("""SELECT from_date, to_date, member_id, COUNT(*) as number_of_transactions, SUM(rent_fee) as total_rent_fee FROM `tabTransactions` GROUP BY member_id ;""")
    return data

def get_columns():
    return [
    "From Date:Date",
    "To Date:Date",
    "Member ID:Data",
    "Number Of Transactions:Int",
    "Total Rent Fee:Int"
  ]