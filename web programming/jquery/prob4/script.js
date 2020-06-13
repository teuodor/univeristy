var list = [["mere", "pere"], [2, 3], [24, 15]]
var first = false
var firstClick = []

function initialize(){
    firstClick.length = list.length
    for(i = 0; i < firstClick.length; i++)
        firstClick[i] = false
    first = true
}

function populate(){

    $("#myTable > tbody > tr > td").each(function(){
        var col = $(this).parent().children().index($(this));
        console.info(col)
        if(col != 0)
            this.remove()
    })
    
    var i = 0
    $("#myTable > tbody > tr").each(function(){
            for(j = 0; j < list[i].length; j++){
                var tdTemplate = "<td>"+ list[i][j] + "</td>";
                var $td = $(tdTemplate)
                console.log($td[0])
                this.append($td[0]);
            }
            i += 1;
    })
   
}

populate()
initialize()

function sort(nr){
    firstClick[nr] = !firstClick[nr]
    for(i = 0; i < list[nr].length - 1; i++)
        for(j = i + 1; j < list[nr].length; j++){
            if((list[nr][i] > list[nr][j]) == firstClick[nr]){
                for(k = 0; k < list.length; k ++)
                    list[k][i] = [list[k][j], list[k][j] = list[k][i]][0];
            } 
        }
    populate()
}