frappe.query_reports["Library Books"] = {
    "filters": [
    {
            "fieldname":"books",
            "label": __("Books"),
            "fieldtype": "Link",
            "options": "Books",
        },
    {
            "fieldname":"members",
            "label": __("Library Members"),
            "fieldtype": "Link",
            "options": "Members",
        },
    {
            "fieldname":"status",
            "label": __("Transaction Status"),
      "default": "",
            "fieldtype": "Select",
            "options": ['', 'Returned', 'Pending Return'],
        },
    ]
}