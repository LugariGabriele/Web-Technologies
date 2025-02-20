function nonBlank(field){
    if(field.value == ""){
        alert("Please enter a value for the '" + field.name + "' field.");
        field.focus();
        return false;
    }
    return true;
}

function validEmail(field){
    var result = false;
    if (nonBlank(field)) {
        var email = new String(field.value);
        var at = email.indexOf("@");
        var dot = email.lastIndexOf(".");
        if (at > 0 && dot > at && dot < email.length - 2) {
            result = true;
        }
    }
    else{
        result=false
    }

    if (!result) {
        alert("Please enter a valid email address in the form");
        field.focus();
    }

    return result;
}
    