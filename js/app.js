(function($, document, window){

	$(document).ready(function(){
		$(".slider").flexslider({
			animation: "fade",
			controlNav: true,
			directionNav: false,
		});

		$(".menu-toggle").click(function(){
			$(".main-navigation .menu").slideToggle();
		});

		$("[data-bg-color]").each(function(){
			var color = $(this).data("bg-color");
			$(this).css("background-color",color);
		});

		new WOW().init();
	});

	$(window).ready(function(){

	});

})(jQuery, document, window);