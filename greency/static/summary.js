$(function() {    
function renderSummaryTable() {


    $('#summaryTable').on("click", "tr", function(){
        var pn = $(this).attr('class');
        //window.location.href = 'http://www.google.com';
        console.log(pn);
    });

}

  $( document ).ready(renderSummaryTable());

  });