var textBoxInit = true;
var tagBoxInit = true;

$(document).ready(
    function(){
        $('#url_input').focus(
            function(){
                if(textBoxInit){
                    $('#url_input').val("");
                    textBoxInit = false;
                }
            });

        $('#url_tag').focus(
            function(){
                if(tagBoxInit){
                    $('#url_tag').val("");
                    tagBoxInit = false;
                }
            });
});
