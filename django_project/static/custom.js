$(function(){

	/* mobile-menu */
	$('.mobile-menu').on('click', function () {
		if ($(this).hasClass('active')) {
			$(this).removeClass('active').addClass('none')	
		} else {
			$(this).removeClass('none').addClass('active')	
		}
	});

	
})

$(function(){
	if( $(document).width() < 992){
		$(".m-menu > a").click(function(){
			return false;
		});
	}
})

