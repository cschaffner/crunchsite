$(function() {

  var $mainNav = $("#main-nav");
  var $subNav = $("#sub-nav");
  var $subNavOther = $("#sub-nav-other");
  var $content = $("#content");
  var $curOther;


  $content.mouseover(function(e) {
    if ($curOther) {
      $curOther.removeClass().addClass('animated flipOutX');
      $curOther = null;
    }
  });

  $mainNav.find('a').mouseover(function(e) {
    var a = $(this);

    var ul = a.next();
    if (ul.length) {
      e.preventDefault();
      _menuChanged = true;
      $curOther = ul.clone();
      $subNavOther.empty().append($curOther);
      $curOther.addClass('animated flipInX');
    }
  });
});