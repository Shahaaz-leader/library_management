import frappe
from frappe import _
from frappe.utils import today

@frappe.whitelist()
def check_days(days):
    doc = frappe.get_doc('Library Settings')
    if int(doc.allowed_number_of_days) < int(days):
        frappe.throw(
            title='Attention',
            msg='Number Of Allowed Days Exceeded.'
            )

def check_debt(transactions, method):
    doc = frappe.get_doc('Members', transactions.member_id)
    settings = frappe.get_doc('Library Settings')
    if doc.outstanding_debt > settings.maximum_outstanding_debt:
        frappe.msgprint('Member has an outstanding debt of Rs'+str(doc.outstanding_debt))
    
@frappe.whitelist()
def cancel_transaction(book_name, rent_fee, member_name):
    book = frappe.get_doc('Books', book_name)
    member = frappe.get_doc('Members', member_name)
    book.number_of_copies = int(book.number_of_copies) + 1
    member.outstanding_debt = int(member.outstanding_debt) - int(rent_fee)
    member.save()
    book.save()
    
@frappe.whitelist()      
def submit_transaction(book_name, member_name, rent_fee):
    book = frappe.get_doc('Books', book_name)
    member = frappe.get_doc('Members', member_name)
    member.outstanding_debt = int(member.outstanding_debt) + int(rent_fee)
    book.number_of_copies = int(book.number_of_copies) - 1
    member.save()
    book.save()

@frappe.whitelist()
def update(book_name, member_name, rent_fee):
    book = frappe.get_doc('Books', book_name)
    member = frappe.get_doc('Members', member_name)
    book.number_of_copies = int(book.number_of_copies) + 1
    member.outstanding_debt = int(member.outstanding_debt) - int(rent_fee)
    member.save()
    book.save()
    frappe.msgprint("Transaction Complete")