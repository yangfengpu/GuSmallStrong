$(function() {
  var fields = ['pn', 'sn', 'type', 'spec', 'package', 'pcs', 'price', 'deliver_day', 'company', 'dayin', 'dayout', 'ps'];
    $( "#dayin" ).datepicker();
    $( "#dayout" ).datepicker();
    $( "#daydeliver" ).datepicker();
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
            console.log(e);
        }
     });
      reset(fields);
    });

    
    $( document ).ready(function() {
        $('#bomTable').tablesort();
    });

    $( "#addARecord" ).click(function() {
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

      return record;
    }
  });
