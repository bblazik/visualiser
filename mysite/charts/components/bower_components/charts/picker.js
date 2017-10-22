$('#datetimepicker10').datetimepicker({
    viewMode: 'years',
    format: 'MM/YYYY'
});
$('#datetimepicker10').on('dp.change', function(e){
    //alert("dupa");
    
    $(this).datetimepicker('hide');
    console.log(e.date.format('DD MM YYYY'));
    $(this).datetimepicker.value = e.date._d;
    document.viewDate.date.value = e.date.format('DD MM YYYY');
    $('#viewDate').submit();
    
});

        