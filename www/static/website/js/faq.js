$(function() {
  var list = $("#faq-items");

  $("#faq-content .plugin").each(function(n){
    var obj = $(this);
    var title = obj.find("h2");
    var titleString = title.html();

    title.html("<a name='faq-item-"+n+"'>" + titleString + "</a>");

    list.append("<li class='list-group-item'><a href='#faq-item-"+n+"'>" + titleString + "</a></li>");
  });

});