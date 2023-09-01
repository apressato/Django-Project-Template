/*
 * Copyright (c) 2020-2023 by APressato <apressato.oss@gmail.com>
 *
 * This file is part of Support_DashBoard.
 * Support_DashBoard is a website to help Support Teams in their work.
 *
 * Support_DashBoard is free software: you can redistribute it and/or modify
 * it under the terms of the
 * Creative Commons Attribution ShareAlike 4.0 International
 * as published by Creative Commons.
 *
 * Support_DashBoard is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY.  See the
 * Creative Commons Attribution ShareAlike 4.0 International for more details.
 *
 * You should have received a copy of the
 * Creative Commons Attribution ShareAlike 4.0 International
 * along with Support_DashBoard. If not,
 * see <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.
 */

$(document).ready(function(){

	$('[data-bs-chart]').each(function(index, elem) {
		this.chart = new Chart($(elem), $(elem).data('bs-chart'));
	});

});