function send_js(num){
        
        //This is the data read from webpage
        num=[num]
        //Parameters for sending data to python
       $.ajax({
         type: "POST",
         contentType: "application/json; charset=utf-8",
         url: "/calculate",
         dataType: "json",
         async: true,
         data: JSON.stringify(num),



        //Get data back from python to send back to webpage
         success: function (data) {
           
          
          document.getElementById('ans').innerHTML = data.result;


         },
         error: function (result) {
          alert("Error");
         }
       })
     }