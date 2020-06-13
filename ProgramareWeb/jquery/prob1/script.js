$(document).ready(function(){
    $("option").dblclick(function () {
    var parent = $(this).parent();
    console.info(parent.attr('id'))
    if(parent.attr('id') == "list1")
        $("#list2").append($(this));
    else
        $("#list1").append($(this));
    }
);})