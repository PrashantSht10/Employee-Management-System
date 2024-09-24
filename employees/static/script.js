// JavaScript for the Employee Management System
function checkdelete() {
    return confirm('Are you sure you want to delete this record?');
}

function validation() {
    var id = document.forms["f1"]["user"].value;
    var ps = document.forms["f1"]["pass"].value;
    if (id === "" && ps === "") {
        alert("User Name and Password fields are empty");
        return false;
    } else {
        if (id === "") {
            alert("User Name is empty");
            return false;
        }
        if (ps === "") {
            alert("Password field is empty");
            return false;
        }
    }
    return true;
}
