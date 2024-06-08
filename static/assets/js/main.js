(function ($) {
  "use strict";
  

	//--Header Menu--//
	$(".header-bar").on("click", function(e) {
		$(".main-menu, .header-bar").toggleClass("active");
	});
	$(".main-menu li a").on("click", function(e) {
		var element = $(this).parent("li");
		if (element.hasClass("open")) {
			element.removeClass("open");
			element.find("li").removeClass("open");
			element.find("ul").slideUp(300, "swing");
		} else {
			element.addClass("open");
			element.children("ul").slideDown(300, "swing");
			element.siblings("li").children("ul").slideUp(300, "swing");
			element.siblings("li").removeClass("open");
			element.siblings("li").find("li").removeClass("open");
			element.siblings("li").find("ul").slideUp(300, "swing");
		}
	});
	//menu top fixed bar
	var fixed_top = $(".header-section");
	$(window).on("scroll", function() {
		if ($(this).scrollTop() > 220) {
			fixed_top.addClass("menu-fixed animated fadeInDown");
			fixed_top.removeClass("slideInUp");
			$("body").addClass("body-padding");
		} else {
			fixed_top.removeClass("menu-fixed fadeInDown");
			fixed_top.addClass("slideInUp");
			$("body").removeClass("body-padding");
		}
	});
	//menu top fixed bar
	$(".scrollToTop").on("click", function() {
		$("html, body").animate({
				scrollTop: 0,
			},
			700
		);
		return false;
	});
	//--Header Menu--//



	// banner-slide area start here
	var sliderActive1 = ".banner__slider";
	var sliderInit1 = new Swiper(sliderActive1, {
		loop: true,
		slidesPerView: 1,
		effect: "fade",
		speed: 2000,
		autoplay: {
		delay: 5000,
		disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
		pagination: {
			el: ".banner-pagination",
			clickable: true,
		},
	});

	// content animation when active slider js start here
	function animated_swiper(selector, init) {
		var animated = function animated() {
			$(selector + " [data-animation]").each(function () {
				var anim = $(this).data("animation");
				var delay = $(this).data("delay");
				var duration = $(this).data("duration");
				$(this)
					.removeClass("anim" + anim)
					.addClass(anim + " animated")
					.css({
						webkitAnimationDelay: delay,
						animationDelay: delay,
						webkitAnimationDuration: duration,
						animationDuration: duration,
					})
					.one("animationend", function () {
						$(this).removeClass(anim + " animated");
					});
			});
		};
		animated();
		init.on("slideChange", function () {
			$(sliderActive1 + " [data-animation]").removeClass("animated");
		});
		init.on("slideChange", animated);
	}
	animated_swiper(sliderActive1, sliderInit1);
	// content animation when active slider js end here

	///============= Scroll To Top =============\\\
	let calcScrollValue = () => {
		let scrollProgress = document.getElementById("progress");
		let progressValue = document.getElementById("valu");
		let pos = document.documentElement.scrollTop;
		let calcHeight =
		document.documentElement.scrollHeight - 
		document.documentElement.clientHeight;
		let scrollValue = Math.round((pos * 250) / calcHeight);
		
		if (pos > 250){
			scrollProgress.style.display = "grid";
		} else{
			scrollProgress.style.display = "none";
		}
		scrollProgress.addEventListener("click", () => {
			document.documentElement.scrollTop = 0;
		}); 
	};
	window.onscroll = calcScrollValue;
	window.onload = calcScrollValue;
    ///============= Scroll To Top =============\\\

    /*-------- Wow Animation Start--------*/
	new WOW().init();
	/*-------- Wow Animation End--------*/

	/*-------- Magnific Popup Start--------*/
	$('.video-btn').magnificPopup({
		type: 'iframe',
		callbacks: {
	  	}
	});
	$(function() {
		$('.g-img').magnificPopup({
		  type: 'image',
		  gallery:{
			enabled:true
		  }
		  });
	  });
	/*-------- Magnific Popup Start--------*/
	
	//classes-slide-area-start-here
	var swiper = new Swiper(".classes__wrapper", {
		spaceBetween: 30,
		speed: 1300,
		centeredSlides: true,
		autoplay: {
		delay: 3000,
		disableOnInteraction: false,
		},
		loop: "true",
		pagination: {
			el: ".dot",
			clickable: true,
		},
		breakpoints: {
			575: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 3,
			},
		},
	});
	//classes-slide-area-end-here

	//gallery-slide-area-start-here
	var swiper = new Swiper(".gallery__wrapper", {
		spaceBetween: 0,
		speed: 1000,
		centeredSlides: true,
		autoplay: {
		delay: 3000,
		disableOnInteraction: false,
		},
		loop: "true",
		pagination: {
			el: ".dot",
			clickable: true,
		},
		breakpoints: {
			575: {
				slidesPerView: 2,
			},
			992: {
				slidesPerView: 3,
			},
		},
	});
	//gallery-slide-area-end-here

	//Testimonial-slide-area-start-here
	var swiper = new Swiper(".testimonial__wrapper", {
		spaceBetween: 30,
		speed: 1000,
		autoplay: {
		delay: 3000,
		disableOnInteraction: false,
		},
		loop: "true",
		pagination: {
			el: ".dot",
			clickable: true,
		},
		breakpoints: {
			575: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 3,
			},
		},
	});
	var swiper = new Swiper(".testimonial__wrapper__two", {
		spaceBetween: 30,
		speed: 1000,
		autoplay: {
		delay: 3000,
		disableOnInteraction: false,
		},
		loop: "true",
		pagination: {
			el: ".dot",
			clickable: true,
		},
		breakpoints: {
			575: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 2,
			},
		},
	});
	//Testimonial-slide-area-end-here

	//service-slide-area-end-here
	$('.insta__wrapper').owlCarousel({
		loop:true,
		autoplay:true,
		margin:0,
		autoplayTimeout: 3000,
		smartSpeed: 1000,
		navText: [
			'<i class="fa-solid fa-arrow-left-long"></i>',
			'<i class="fa-solid fa-arrow-right-long"></i>'
		],
		responsive:{
		0:{
			items:2
		},
		600:{
			items:3
		},
		1000:{
			items:4
		},
		1199:{
			items:10
		}
		}
	});
	//service-slide-area-end-here

	// choose swiper slider area start here
	var swiper = new Swiper(".choose__slide__two", {
		speed: 1000,
		loop: true,
		spaceBetween: 10,
		slidesPerView: 5,
		freeMode: true,
		autoplay:true,
		watchSlidesProgress: true,
		navigation: {
			nextEl: ".right-arry",
			prevEl: ".left-arry",
		},
	});
	var swiper2 = new Swiper(".choose__slide__one", {
		speed: 1000,
		loop: "true",
		grabCursor: true,
		autoplay:true,
		navigation: {
			nextEl: ".right-arry",
			prevEl: ".left-arry",
		},
		thumbs: {
			swiper: swiper,
		},
	});
	// choose swiper slider area end here

	/*-------- Odometer Counter Start--------*/
	$(".odometer__item").each(function () {
		$(this).isInViewport(function (status) {
			if (status === "entered") {
				for (
					var i = 0;
					i < document.querySelectorAll(".odometer").length;
					i++
				) {
					var el = document.querySelectorAll(".odometer")[i];
					el.innerHTML = el.getAttribute("data-odometer-final");
				}
			}
		});
	});
	/*-------- Odometer Counter End--------*/

	/*-------- Price Range Start--------*/
	//
    function getVals() {
        // Get slider values
        let parent = this.parentNode;
        let slides = parent.getElementsByTagName("input");
        let slide1 = parseFloat(slides[0].value);
        let slide2 = parseFloat(slides[1].value);
        // Neither slider will clip the other, so make sure we determine which is larger
        if (slide1 > slide2) {
            let tmp = slide2;
            slide2 = slide1;
            slide1 = tmp;
        }

        let displayElement = parent.getElementsByClassName("rangeValues")[0];
        displayElement.innerHTML = "$" + slide1 + " - $" + slide2;
    }

    window.onload = function() {
        // Initialize Sliders
        let sliderSections = document.getElementsByClassName("range-slider");
        for (let x = 0; x < sliderSections.length; x++) {
            let sliders = sliderSections[x].getElementsByTagName("input");
            for (let y = 0; y < sliders.length; y++) {
                if (sliders[y].type === "range") {
                    sliders[y].oninput = getVals;
                    // Manually trigger event first time to display values
                    sliders[y].oninput();
                }
            }
        }
    }
	/*-------- Price Range End--------*/

	// cart popup //
    // cart
    let quantity = 0;
    let price = 0;
    $(".cart-item-quantity-amount, .product-quant").html(quantity);
    $(".total-price, .product-pri").html(price.toFixed(2));
    $(".cart-increment, .cart-incre").on("click", function() {
        if (quantity <= 4) {
            quantity++;
            $(".cart-item-quantity-amount, .product-quant").html(quantity);
            var basePrice = $(".base-price, .base-pri").text();
            $(".total-price, .product-pri").html((basePrice * quantity).toFixed(2));
        }
    });

    $(".cart-decrement, .cart-decre").on("click", function() {
        if (quantity >= 1) {
            quantity--;
            $(".cart-item-quantity-amount, .product-quant").html(quantity);
            var basePrice = $(".base-price, .base-pri").text();
            $(".total-price, .product-pri").html((basePrice * quantity).toFixed(2));
        }
    });

    $(".cart-item-remove>a").on("click", function() {
        $(this).closest(".cart-item").hide(300);
    });
	
	// payment method
    var paymentMethod = $("input[name='pay-method']:checked").val();
    $(".payment").html(paymentMethod);
    $(".checkout__radio-single").on("click", function() {
        var paymentMethod = $("input[name='pay-method']:checked").val();
        $(".payment").html(paymentMethod);
    });

	//search-area-start-here
	var $searchWrap = $(".search-wrap");
	var $navSearch = $(".nav-search");
	var $searchClose = $("#search-close");

	$(".search-trigger").on("click", function (e) {
		e.preventDefault();
		$searchWrap.animate({ opacity: "toggle" }, 500);
		$navSearch.add($searchClose).addClass("open");
	});

	$(".search-close").on("click", function (e) {
		e.preventDefault();
		$searchWrap.animate({ opacity: "toggle" }, 500);
		$navSearch.add($searchClose).removeClass("open");
	});

	function closeSearch() {
		$searchWrap.fadeOut(200);
		$navSearch.add($searchClose).removeClass("open");
	}

	$(document.body).on("click", function (e) {
		closeSearch();
	});

	$(".search-trigger, .main-search-input").on("click", function (e) {
		e.stopPropagation();
	});
	//search-area-end-here
	
	/*---------- Logo Section ----------*/
$('.logo-wrapper').owlCarousel({
    loop:true,
    autoplay:true,
    margin:30,
    navText: [
        '<i class="fa-solid fa-arrow-left-long"></i>',
        '<i class="fa-solid fa-arrow-right-long"></i>'
    ],
    responsive:{
    0:{
        items:2
    },
        576:{
            items:3
        },
        600:{
            items:4
        },
        1000:{
            items:6
        },
        1199:{
            items:6
        }
    }
});
/*---------- Logo Section ----------*/
//contact form js
	$(function () {
		// Get the form.
		var form = $("#contact-form");
		// Get the messages div.
		var formMessages = $(".form-message");
		// Set up an event listener for the contact form.
		$(form).submit(function (e) {
			// Stop the browser from submitting the form.
			e.preventDefault();
			// Serialize the form data.
			var formData = $(form).serialize();
			// Submit the form using AJAX.
			$.ajax({
				type: "POST",
				url: $(form).attr("action"),
				data: formData,
			})
				.done(function (response) {
					// Make sure that the formMessages div has the 'success' class.
					$(formMessages).removeClass("error");
					$(formMessages).addClass("success");
					// Set the message text.
					$(formMessages).text(response);
					// Clear the form.
					$("#form input, #form textarea").val("");
				})
				.fail(function (data) {
					// Make sure that the formMessages div has the 'error' class.
					$(formMessages).removeClass("success");
					$(formMessages).addClass("error");
					// Set the message text.
					if (data.responseText !== "") {
						$(formMessages).text(data.responseText);
					} else {
						$(formMessages).text(
							"Oops! An error occured and your message could not be sent."
						);
					}
				});
		});
	});

})(jQuery);