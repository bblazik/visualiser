window.onkeyup = function(e) {
    var key = e.keyCode ? e.keyCode : e.which;
    
    if (key == 37) { // left
        document.getElementById('pm').click();
    }else if (key == 39) { //right
         document.getElementById('nm').click();
         
        //$('#nm').submit();
    }else if (key==72){
        // $("#menu-toggle").click(function(e) {
        //     e.preventDefault();
        //     $("#wrapper").toggleClass("toggled");
        // });
        document.getElementById('menu-toggle').click();
    }
    
    
}