var dateNow = new Date();
var bool = true;
$('#datetimepicker4').datetimepicker({
    defaultDate:dateNow,
});
$('#datetimepicker4').on('dp.change', function(e){
    // alert("dupa");
    $(this).datetimepicker('hide');
    console.log(e.date._d);

    $(function () {
        $('#my_hidden_input').val("fgg");
      });

      $('#viewDate').submit();
    
});

