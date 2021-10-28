frappe.ui.form.on('Books', {
	number_of_copies(frm, cdt, cdn) {
	  if (frm.doc.number_of_copies > 0){
		frappe.model.set_value(cdt, cdn, "status", "Available")
	  } else {
		frappe.model.set_value(cdt, cdn, "status", "Not Available")
	  }
  
	 },
  });
  
  frappe.ui.form.on('Books', {
	refresh: function(frm) {
	  frm.add_custom_button(__("Rent This Book"), function(){
		  frappe.prompt([
	  {
		label: 'Member',
		fieldname: 'member',
		fieldtype: 'Link',
		options: 'Members',
	  },
	  ], (values) => {
		if(frm.doc.status == "Available"){
		frappe.new_doc("Transactions", {"book_name": frm.doc.name}, doc => {
		  doc.from_date = frappe.datetime.get_today();
		  doc.member_id = values.member;
		});
	  } else {
		frappe.throw("This Book Is Currently Unavailable.")
	  }
		
	  });
		});
	},
	});