(function($) {
	'use strict';

	var browserWindow = $(window);

	// :: 1.0 Preloader Active Code
	browserWindow.on('load', function() {
		$('#preloader').fadeOut('slow', function() {
			$(this).remove();
		});
	});

	$('[data-delay]').each(function() {
		var anim_del = $(this).data('delay');
		$(this).css('animation-delay', anim_del);
	});

	$('[data-duration]').each(function() {
		var anim_dur = $(this).data('duration');
		$(this).css('animation-duration', anim_dur);
	});

	// :: 8.0 wow Active Code
	if (browserWindow.width() > 767) {
		new WOW().init();
	}
	// :: 2.0 Sticky Active Code
	if ($.fn.sticky) {
		$('.header-sticky').sticky({
			topSpacing : 0
		});
	}

	// :: 3.0 AJAX Like Option

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + '=') {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
	}
	$.ajaxSetup({
		beforeSend : function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader('X-CSRFToken', csrftoken);
			}
		}
	});
	$(document).on('click', '#like', function(event) {
		event.preventDefault();
		var this_ = $(this);
		var course_slug = this_.attr('value');
		var likeForm = this_.closest('form');
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
		$.ajax({
			url      : likeForm.attr('action'),
			method   : 'POST',
			data     : {
				course_slug : course_slug,
				csrftoken   : csrftoken
			},
			dataType : 'json',
			success  : function(response) {
				$('#like-section').html(response['form']);
				console.log(response);
			},
			error    : function(error) {
				console.log(error);
			}
		});
	});

	// :: 4.0 Instructor Page tab
	initTabs();
	function initTabs() {
		if ($('.tab').length) {
			$('.tab').on('click', function() {
				$('.tab').removeClass('active');
				$(this).addClass('active');
				var clickedIndex = $('.tab').index(this);

				var panels = $('.tab_panel');
				panels.removeClass('active');
				$(panels[clickedIndex]).addClass('active');
			});
		}
	}

	/*  
		:: 5.0 Init Accordions
	*/
	initAccordions();
	function initAccordions() {
		if ($('.accordion').length) {
			var accs = $('.accordion');

			accs.each(function() {
				var acc = $(this);

				if (acc.hasClass('active')) {
					var panel = $(acc.next());
					// var panelH = panel.prop('scrollHeight') + 'px';

					if (panel.css('max-height') == '0px') {
						panel.css('max-height', panel.prop('scrollHeight') + 'px');
					} else {
						panel.css('max-height', '0px');
					}
				}

				acc.on('click', function() {
					if (acc.hasClass('active')) {
						acc.removeClass('active');
						var panel = $(acc.next());
						// var panelH = panel.prop('scrollHeight') + 'px';

						if (panel.css('max-height') == '0px') {
							panel.css('max-height', panel.prop('scrollHeight') + 'px');
						} else {
							panel.css('max-height', '0px');
						}
					} else {
						acc.addClass('active');
						var panel = $(acc.next());
						// var panelH = panel.prop('scrollHeight') + 'px';

						if (panel.css('max-height') == '0px') {
							panel.css('max-height', panel.prop('scrollHeight') + 'px');
						} else {
							panel.css('max-height', '0px');
						}
					}
				});
			});
		}
	}
})(jQuery);
