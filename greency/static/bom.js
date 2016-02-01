$(function() {
  var fields = ['pn', 'sn', 'type', 'spec', 'package', 'pcs', 'price', 'deliver_day', 'company', 'dayin', 'dayout', 'ps'];
    $( "#dayin" ).datepicker();
    $( "#dayout" ).datepicker();
    $( "#daydeliver" ).datepicker();
    $( "#add" ).click(function(){
      alert($('select[name="unit"]').val());
      alert($('input[name="dayin"]').val());
      getRecord(fields);
      reset(fields);
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
      var record = new Map();
      for(key in fields){
        record.set(fields[key], $('input[name="' + fields[key] + '"]').val());
      }
      console.log(record);
      return record;
    }
  });
