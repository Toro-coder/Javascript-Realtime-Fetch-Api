function startLiveUpdate(){

    var curr = new Date; // get current date
    var first = curr.getDate() - curr.getDay(); // First day is the day of the month - the day of the week
    var last = first + 6; // last day is the first day + 6

    var firstday = new Date(curr.setDate(first)).toUTCString();
    var lastday = new Date(curr.setDate(last)).toUTCString();

    $.ajax({
        url: "http://127.0.0.1:5000/fetchUsers",
        type: "post",
        data: "y",
        success: function (response) {
           var data = JSON.stringify(response);
           data = data.substring(19);
           data = data.substring(0, data.length - 3);
           document.getElementById("counts").innerHTML = data;
        },
        error: function(jqXHR, textStatus, errorThrown) {
           console.log(textStatus, errorThrown);
        }
    });
}

setInterval(function(){
    startLiveUpdate();
}, 6000);

document.addEventListener('DOMContentLoaded', function(){
    startLiveUpdate();
})

