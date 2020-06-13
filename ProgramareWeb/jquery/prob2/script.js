function validate(){
    var name_txt = $("#name_txt");
    var date_txt = $("#date_txt");
    var age_txt = $("#age_txt");
    var email_txt = $("#email_txt");

    var Name = $("#Name");
    var Date = $("#Date");
    var Age = $("#Age");
    var Email = $("#Email");

    var name = name_txt.val();
    var date = date_txt.val();
    var age = age_txt.val();
    var email = email_txt.val();

    var alert_begin = "Campurile "; 
    var fields = "";
    var alert_end = " nu sunt completate corespunzator";

    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if(name === ""){
        fields = fields.concat("nume, ");
        Name.addClass("notValid")

    }       
    else{
        Name.removeClass();
    }
    
    if(isNaN(age) || age === ""){
        fields = fields.concat("varsta, ")
        Age.addClass("notValid")
    }
    else{
        Age.removeClass()
    }

    if(date === ""){
        fields = fields.concat("data, ")
        Date.addClass("notValid")
    }
    else{
        var date_fields = date.split("/");
        if(date_fields.length == 3){
            for(i = 0; i < date_fields.length; i++)
                if(isNaN(date_fields[i])){
                    fields = fields.concat("data, ")
                    Date.addClass("notValid")
                    break
                }
                Date.removeClass()
        }
        else{
            fields = fields.concat("data, ")
            Date.addClass("notValid")
        }
    }

    if(!email.match(mailformat)){
        fields = fields.concat("email, ")
        Email.addClass("notValid")
    }
    else{
        Email.removeClass()
    }

    if(fields != ""){
        fields.substring(0, fields.length - 2)
        alert(alert_begin + fields + alert_end);
    }
    else{
        alert("Datele sunt completate corect!!!")
    }
}