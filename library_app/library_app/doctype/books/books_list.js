frappe.listview_settings['Books'] = {
    add_fields: ["status", "number_of_copies"],
    get_indicator: function(doc) {
      if(doc.number_of_copies > 0) {
        return [__("Available"), "green", "number_of_copies,>,0"];
      } else if(doc.number_of_copies == 0) {
        return [__("Not Available"), "red", "number_of_copies,==,0"];
      }
    }
  };