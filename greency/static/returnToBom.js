$(function(){

function addReturnToBom(){
    if ($("#backToBom").length > 0){ 
    $("#backToBom").on('click', function(){
        var base_url = window.location.origin;
        window.location.href = base_url + "/bom";
        });
    } 
   }

  $( document ).ready(addReturnToBom());


});
