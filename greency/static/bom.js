$(function() {
  var fields = ['pn', 'sn', 'type', 'spec', 'package', 'pcs', 'price', 'deliver_day', 'company', 'dayop', 'operation_type', 'ps'];
    $( "#dayop" ).datepicker();
    
    $( "#add" ).click(function(){

      var rec = getRecord(fields);
      console.log(JSON.stringify(rec));
      $.ajax({
        type: 'POST',
        // Provide correct Content-Type, so that Flask will know how to process it.
        contentType: 'application/json',
        // Encode your data as JSON.
        data: JSON.stringify(rec),
        // This is the type of data you're expecting back from the server.
        dataType: 'json',
        url: '/gugupost',
        success: function (e) {
            window.location = location.href;
        },
        error: function(e){
          console.log(e);
          window.location = location.href;
        }
     });
    });

    $('.delete_data').click(function(e){
        event.stopPropagation();
        var oid = $(e.target).attr('data_id');
        console.log();
        console.log('delete');

        $.ajax({
          type: 'GET',
          dataType: 'json',
          url: '/guguremove/'.concat(oid),
          success: function (e) {
              window.location = location.href;
          },
          error: function(e){
            console.log(e);
            window.location = location.href;
          }
       });


      }
    );

    $('.edit_data').click(function(e){
        event.stopPropagation();
        console.log($(e.target).attr('data_id'));
        console.log('edit');
      }
    );

    function renderTable() {
        $('#bomTable').tablesort();
        $('#bomTable').delegate("tr", "click", function(){
          var rowId = $(this).attr('class');
          console.log(rowId);
          var cells = this.querySelectorAll("td");
          var cellData = [];
          for (var i = 1; i < cells.length; i+=1) {
            var cell = cells[i].firstChild;
            if(cell){
              //console.log(cell.data);
              cellData[i-1] = cell.data;
            }else{
              //console.log('null');
              cellData[i-1] = '';
            }
          }
          console.log(cellData);
          setReuseData(fields, cellData);
          $('.ui.modal').modal('show');

        });
    }
    
    $( document ).ready(renderTable());
    $( document ).ready(addReturnToBomSummary());

    $( "#addARecord" ).click(function() {
      reset(fields);
     /*
      $.ajax({
      method: "GET",
      url: "testJson",
      //data: { name: "John", location: "Boston" }
    })
      .done(function( msg ) {
        alert( "Data Saved: " + msg.a );
      });
    */
    $('.ui.modal').modal('show');
      });

    function reset(fields){
      for(key in fields ){
          $('input[name="' + fields[key] + '"]').val("");

        
      }
      
    }

    function setReuseData(fields, reuseData){
      for(key in fields ){
          $('input[name="' + fields[key] + '"]').val(reuseData[key]);
        
        
      }
      
    }


    function getRecord(fields){
      /*
      var record = new Map();
      for(key in fields){
        record.set(fields[key], $('input[name="' + fields[key] + '"]').val());
      }*/
      var record = {};
      for (key in fields){
        record[fields[key]] = $('input[name="' + fields[key] + '"]').val();
      }
      record['unit'] = $('select[name="unit"]').val();
      record['operation_type'] = $('select[name="operation_type"]').val();

      return record;
    }

   function addReturnToBomSummary(){
    if ($("#bomSummary").length > 0){ 
    $("#bomSummary").on('click', function(){
        var base_url = window.location.origin;
        window.location.href = base_url + "/summary";
    });
} 
   }
  });
