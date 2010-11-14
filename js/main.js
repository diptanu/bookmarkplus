var textBoxInit = true;

$(document).ready(
    function(){
        $('#url_input').focus(
            function(){
                if(textBoxInit){
                    $('#url_input').val("");
                    textBoxInit = false;
                    
                }
            });
});
