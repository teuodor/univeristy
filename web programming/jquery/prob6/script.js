
var current_x
var current_y
var table
var clicked = false
var n = 0
var first = false
var _row

initialize()

$(this).keydown(function(event) {
if(clicked){
    switch (event.keyCode) {
    case 37:
            if(current_y != 0){
                current_y -= 1
                var emptyCell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html();
                var cell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + (current_y + 1) + ")").html();
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html(cell)
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + (current_y + 1) + ")").html(emptyCell)
            }
        break;
    case 38:
            if(current_x != 0){
                current_x -= 1
                var emptyCell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html();
                var cell = $("#myTable").find("tr:eq(" + (current_x + 1) + ") td:eq(" + current_y + ")").html();
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html(cell)
                $("#myTable").find("tr:eq(" + (current_x + 1) + ") td:eq(" + current_y + ")").html(emptyCell)
            }
        break;
    case 39:
            if(current_y != n - 1){
                current_y += 1
                var emptyCell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html();
                var cell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + (current_y - 1) + ")").html();
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html(cell)
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + (current_y - 1) + ")").html(emptyCell)
            }
        break;
    case 40:
            if(current_x != n - 1){
                current_x += 1
                var emptyCell = $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html();
                var cell = $("#myTable").find("tr:eq(" + (current_x - 1) + ") td:eq(" + current_y + ")").html();
                $("#myTable").find("tr:eq(" + current_x + ") td:eq(" + current_y + ")").html(cell)
                $("#myTable").find("tr:eq(" + (current_x - 1) + ") td:eq(" + current_y + ")").html(emptyCell)
                
            }
        break;
    }
    if(current_x === n - 1 && current_y === n - 1){
        verify()
    }
}
}
)

function initialize(){
    table = $("#myTable");
    _row = $("#myTable tr")
    clicked = true
}

function send_click(){
    var txt = $("#text").val()
    if(isNaN(txt)){
        clicked = false
    }
    else{
        n = parseInt(txt)
        if(n > 1)
            initialize()
            generate_game()
            first = true
    }
    
}
function verify(){
    var ok = true
    var tmp = 1
    $("#myTable > tr > td").each(function () { 
        var tdata = $(this);
         if(tdata.html() != tmp && tmp != n*n){
             ok = false;
         }
         tmp++;
    });
    if(ok){
        ok = confirm("You've finished the game. Another one?")
        if(ok){
            generate_game()
        }
    }
}
function generate_game(){
    
    if(first){
        $("#myTable").empty();
    }

    current_x = n - 1
    current_y = n - 1

    var list = []
    list.length = n*n - 1
    for(i = 1; i < n*n; i++){
        list[i - 1] = i
    }
    list = shuffle(list)

    var tmp = 0
    for(i = 0; i < n; i++){
        var rowTemp = "<tr>";
        for(j = 0; j < n; j++){
            if(i == n - 1 && j == n - 1)
                rowTemp += "<td></td>";
            else
                rowTemp += "<td>" + list[tmp] + "</td>";
            tmp++
        }
        rowTemp += "</tr>";
        var row = $(rowTemp);
        $("#myTable").append(row[0]);
    }

}

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (0 !== currentIndex) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}