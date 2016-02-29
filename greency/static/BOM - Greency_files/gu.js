
$(document).ready(function() {

   /* 
    $.ajax({
        url : 
    });
   */

     var logout = function(){
       $.ajax({url : '/logout'}).done(function (data){
           window.location.href = "/login";
       });
     };

     $('#logout').click(logout);

     $('.ui.checkbox').checkbox();
     


});