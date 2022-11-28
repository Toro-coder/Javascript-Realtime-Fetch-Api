function startLiveUpdate(route) {
    $.ajax({
        url: "http://127.0.0.1:5000/" + route,
        type: "POST",
        data: "y",
        success: function (response) {
        var data = JSON.stringify(response);
        data = data.substring(10); // removes the first 19 characters
            data = data.substring(0, data.length - 2); // removes the last 3 characters
            data = data.split(",");
        // stringify total and weekly users
        if(route === "fetchUsers"){
           document.getElementById("counts").innerHTML += data + "<br><br>";
        }
        // stringify county users
        else if(route === "countyusers"){
           for(var i=0; i <= 93; i++) {
               if(i % 2) {
                   document.getElementById("counts").innerHTML += data[i].substring(0, data[i].length - 1) + "<br><br>";
//
               } else {
                   document.getElementById("counts").innerHTML += data[i].substring(2, data[i].length - 1) + " " ;
               }

           }
        }
        // stringify gender
        else if (route === "gender"){
            for(var i=0; i <= 6; i++) {
               if(i % 2) {
                   document.getElementById("counts").innerHTML += data[i].substring(0, data[i].length - 1) + "<br><br>";
//
               } else {
                   document.getElementById("counts").innerHTML += data[i].substring(2, data[i].length - 1) + " " ;
               }

           }
        }
       // stringify gender
       else if (route === "age_range"){

            for(var i=0; i <= 14; i++) {
               if(i % 2) {
                   document.getElementById("counts").innerHTML += data[i].substring(0, data[i].length - 1) + "<br><br>";
//
               } else {
                   document.getElementById("counts").innerHTML += data[i].substring(2, data[i].length - 1) + " " ;
               }
           }
       }
        }
//        error: function(jqXHR, textStatus, errorThrown) {
//           console.log(textStatus, errorThrown);
//        }
    });
}

setInterval(function() {
    startLiveUpdate("fetchUsers");
    startLiveUpdate("countyusers");
    startLiveUpdate("gender");
    startLiveUpdate("age_range");

}, 6000);

document.addEventListener('DOMContentLoaded', function(){
    startLiveUpdate();
})

