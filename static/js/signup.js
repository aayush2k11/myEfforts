// JavaScript Document
$(document).ready(function(e) {
	$('.form input').attr("value","");
	$('.form input[type=submit]').attr("value","Join Us");
    $('.form').submit(function(){
		if ($('.form input[name=disnam]').val()=='')
		{
			$('.form input[name=disnam]').attr("placeholder",'You must provide display name');
			$('.form input[name=disnam]').css("color","yellow");
			$('.form input[name=disnam]').focus();
			// 	alert('You must provide display name');
			return false;
			}
		if ($('.form input[name=email]').val()=='')
		{
			$('.form input[name=disnam]').css("color","white");
			$('.form input[name=email]').attr("placeholder",'You must provide email');
			$('.form input[name=email]').css("color","yellow");
			$('.form input[name=email]').focus();
			return false;
			}
		else if ($('.form input[name=password]').val()=='')
		{
			$('.form input[name=disnam]').css("color","white");
			$('.form input[name=email]').css("color","white");
			$('.form input[name=password]').attr("placeholder",'You must provide password');
			$('.form input[name=password]').css("color","yellow");
			$('.form input[name=password]').focus();
			return false;
			}
		else if ($('.form input[name=cnfpassword]').val()!==$('.form input[name=password]').val())
		{
			$('.form input[name=disnam]').css("color","white");
			$('.form input[name=email]').css("color","white");
			$('.form input[name=password]').css("color","white");
			$('.form input[name=cnfpassword]').attr("placeholder",'Passwords do not match');
			$('.form input[name=cnfpassword]').css("color","yellow");
			$('.form input[name=cnfpassword]').focus();
			return false;
			}
		});
});