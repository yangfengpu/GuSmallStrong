    function repeat(operation, num) {
      // SOLUTION GOES HERE
      if (num === 0){
          //stop
      }else{
          
        operation();
        var nextnum = num - 1;
        repeat(operation, nextnum);
      }


    }

    // Do not remove the line below
    module.exports = repeat