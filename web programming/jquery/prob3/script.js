var first_image = null
var second_image = null
function memory_game(i){
    image = $(i);
    if(!image.hasClass("hidden"))
        return
    
    if(first_image === null && second_image === null ){
        first_image = image
        image.removeClass("hidden")
    }
    else if(first_image != null && second_image === null ){
        second_image = image
        second_image.removeClass("hidden")
    }
    else if(first_image != null && second_image != null ){
        if(first_image.attr('src') != second_image.attr('src')){
            first_image.addClass("hidden")
            second_image.addClass("hidden")
        }
        first_image = null
        second_image = null
        image.removeClass("hidden")
        first_image = image
    }
}