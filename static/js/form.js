$('#new_bookmark').submit(function(){
  var url = $('#url_text').val();
  var tags = $('#url_tag').val();
  var text = $('#url_description').val();
  
  $.post("/ajax/new_bookmark/", {'url_text': url, 'url_tag': tags, 'description': text}, function(data){
    var result = $.parseJSON(data)
    if(result.result){
      $('#save_success_msg').html("The Bookmark has been added").show();
      $('#form_bookmark').hide();
    }
  })
  return false;
});
