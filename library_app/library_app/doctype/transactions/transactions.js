frappe.ui.form.on("Transactions",{
	to_date(frm,cdt,cdn){
	  frappe.model.set_value(cdt,cdn, "number_of_days", frappe.datetime.get_day_diff(frm.doc.to_date, frm.doc.from_date));
	  frappe.call({
		method: "library_app.api.check_days",
		args: {
		  'doctype': "Transactions",
		  'days': frm.doc.number_of_days
		},
	  });
  },
  number_of_days(frm,cdt,cdn){
	frappe.db.get_single_value('Library Settings', 'rent_fee')
	  .then(rent_fee => {
		  let rent = rent_fee * frm.doc.number_of_days
	  frappe.model.set_value(cdt,cdn, "rent_fee", rent)
	  });
  },
  on_submit(frm){
	frappe.call({
	  method: "library_app.api.submit_transaction",
	  args: {
		
		'member_name': frm.doc.member_id,
		'rent_fee': frm.doc.rent_fee,
		'book_name': frm.doc.book_name,
	  },
	});
  },
  after_cancel(frm){
	frappe.call({
	  method: "library_app.api.cancel_transaction",
	  args: {
		
		'member_name': frm.doc.member_id,
		'rent_fee': frm.doc.rent_fee,
		'book_name': frm.doc.book_name
	  },
	});
  },
  onload: function(frm) {
	frm.set_query("book_name", function() {
	  return {
		"filters": {
		  "status": 'Available',
		}
			  };
		  });
	  },
  });
  
  frappe.ui.form.on('Transactions', {
	refresh: function(frm) {
	  frm.add_custom_button(__("Return Book"), function(){
		frappe.call({
		  method: "library_app.api.update",
		  args: {
			
			'member_name': frm.doc.member_id,
			'rent_fee': frm.doc.rent_fee,
			'book_name': frm.doc.book_name
		  },
		});
		});
	},
	});