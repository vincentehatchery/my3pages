function displayDate()
{
	var d = new Date();
	var curr_date = d.getDate();
		if (curr_date < 10){
			curr_date = "0" + curr_date;
		}
	var curr_month = d.getMonth() + 1; //Months start at 0
		if (curr_month < 10){
			curr_month = "0" + curr_month;
		}
	var curr_year = d.getFullYear();
		
	var formatted_date = curr_year + "-" + curr_month + "-" + curr_date
	return formatted_date;
	
};
//Display the javascript date and time in the form
var a=document.getElementById('date_entered');
//a.innerHTML=displayDate();
a.value = displayDate();