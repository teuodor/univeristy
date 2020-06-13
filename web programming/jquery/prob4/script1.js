
var list = [["mere", "pere"], [2, 3],[24, 15]]
var first = false
var click = []

function initialize(){
    click.length[0] = list.length
    for(i = 0; i < click.length; i++)
        click[i] = false
    first = true
}

function populate(){
    $("#myTable > tbody > tr > td").each(function(){
        var row = $(this).parent().parent().children().index($(this).parent());
        console.info(row)
        if(row != 0)
            this.remove()
    })
    
    var i = 0
    for(i = 0; i < list[0].length; i++){
        var rowTemp = "<tr>";
        for(j = 0; j < list.length; j++){
            rowTemp += "<td>" + list[j][i] + "</td>";
        }
        rowTemp += "</tr>";
        var row = $(rowTemp);
        $("#myTable").append(row[0]);
    }

}

populate()
initialize()

function sort(nr){
    click[nr] = !click[nr]
    for(i = 0; i < list[nr].length - 1; i++)
            for(j = i + 1; j < list[nr].length; j++){
                if((list[nr][i] > list[nr][j]) == click[nr]){
                    for(k = 0; k < list.length; k ++)
                        list[k][i] = [list[k][j], list[k][j] = list[k][i]][0];
                } 
            }
        populate()
}
