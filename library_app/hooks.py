from __future__ import unicode_literals
from . import __version__ as app_version


app_name = "library_app"
app_title = "Library App"
app_publisher = "Shahaaz"
app_description = "Library Management app"
app_icon = "octicon octicon-file-directory"
app_color = "Blue"
app_email = "m.shahaaz@leadergroup.com"
app_license = "MIT"

# include js, css files in header of desk.html
app_include_css = [
    "/assets/bdtheme/css/bdtheme.css",
    "/assets/bdtheme/css/skin-blue.css",
    "/assets/bdtheme/css/custom.css",
    "/assets/bdtheme/css/temp.css",
]
app_include_js = [
    "/assets/bdtheme/js/bdtheme.js",
    "/assets/bdtheme/js/custom.js",
    "/assets/js/bdtheme-template.min.js",
]

# include js, css files in header of web template
web_include_css = "/assets/bdtheme/css/bdtheme-web.css"
# web_include_js = "/assets/bdtheme/js/bdtheme.js"









# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_app/css/library_app.css"
# app_include_js = "/assets/library_app/js/library_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_app/css/library_app.css"
# web_include_js = "/assets/library_app/js/library_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library_app.install.before_install"
# after_install = "library_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Transactions": {
		"validate": "library_app.api.check_debt"
	}
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_app.tasks.all"
# 	],
# 	"daily": [
# 		"library_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"library_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "library_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_app.auth.validate"
# ]

