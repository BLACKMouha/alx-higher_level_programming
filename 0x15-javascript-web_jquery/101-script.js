#!/usr/bin/node
$(window).on('load', function () {
	$('#add_item').on('click', function () {
		$('.my_list').append('<li>Item</li>');
	});

	$('#remove_item').on('click', function () {
		$('.my_list li:last-child').remove();
	});

	$('#clear_list').on('click', function () {
		$('.my_list').empty();
	});
});
