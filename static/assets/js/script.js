$(document).ready(function(){$("#owl-example").owlCarousel(),$(".listing-detail span").tooltip("hide"),$(".carousel").carousel({interval:3e3}),$(".carousel").carousel("cycle")}),$(function(){var n=function(){var n=$("#nav-dots > span"),e=$("#slider").slitslider({onBeforeChange:function(e,t){n.removeClass("nav-dot-current"),n.eq(t).addClass("nav-dot-current")}}),t=function(){o()},o=function(){n.each(function(t){$(this).on("click",function(o){var a=$(this);return e.isActive()||(n.removeClass("nav-dot-current"),a.addClass("nav-dot-current")),e.jump(t+1),!1})})};return{init:t}}();n.init()});