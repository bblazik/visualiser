window.onkeyup = function(e) {
    var key = e.keyCode ? e.keyCode : e.which;
    
    if (key == 37) { // left
        document.getElementById('pm').click();
    }else if (key == 39) { //right
         document.getElementById('nm').click();
         
        //$('#nm').submit();
    }
    
    
}