$(document).ready(function(){
    $('.date').mask('00/00/0000');
});

$(document).ready(function(){
  $('#select').on('change', function(){
    
    var selectValor = '#'+$(this).val();
    
    $('#racas').children('div').hide();
    $('#racas').children(selectValor).show();
  
  });
});
  