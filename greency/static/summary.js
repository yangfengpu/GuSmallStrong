$(function() {    
function renderSummaryTable() {


    $('#summaryTable').on("click", "tr", function(){
        var pn = $(this).attr('class');
        var base_url = window.location.origin;
        window.location.href = base_url + "/bomByPn/" + pn
        console.log(pn);
    });

}

  $( document ).ready(renderSummaryTable());

  });