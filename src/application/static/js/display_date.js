function displayDate()
{
	var d = new Date();
	return d;
	
};
//Display the javascript date and time in the form
var a=document.getElementById('date_entered');
//a.innerHTML=displayDate();
a.value =displayDate();