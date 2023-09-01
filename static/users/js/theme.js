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

(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

})(jQuery); // End of use strict
