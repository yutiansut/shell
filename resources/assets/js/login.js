$(document).on("click", ".submit", function (){
    var username = $("input[name=username]").val();
    var password = $("input[name=password]").val();
    $.post("/login", {
        "username": username,
        "password": password
    }, function (response) {
        console.log(response); 
    }, "json");
});
