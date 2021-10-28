// Copyright (c) 2016, Shahaaz and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Books Report"] = {
	"filters": [
		{
            "fieldname":"books",
            "label": __("Book Name"),
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
};
