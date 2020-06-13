
var slideIndex = 1;
showSlides(slideIndex);

var timeoutHandle = setTimeout(()=>{plusSlides(1);}, 2000);

function plusSlides(n) {
    showSlides(slideIndex += n);
    clearTimeout(timeoutHandle);
    timeoutHandle = setTimeout(()=>{plusSlides(1);}, 2000);
}

function showSlides(n) {
    var length = 0;
    $(".mySlides").each(function(){
        length += 1
    });

    if (n > length) {slideIndex = 1}    
    if (n < 1) {slideIndex = length}

    var i = 1
    $(".mySlides").each(function(){
        lis = $(this)
        console.log(lis)
        if(slideIndex == i){
            lis.css("display", "block");
        }
        else{
            lis.css("display", "none");
        }
        i++;
    })
}