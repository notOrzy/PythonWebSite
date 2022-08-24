$(window).scroll(function() {

	var scrollPos = $(this).scrollTop();
	console.log(scrollPos);
	$('.pyw .pythonlogo').css({
		'width': 300 - scrollPos/4
	})

})