$(document).ready(function(){
  $('.mask-date').mask('00/00/0000');

  $('#id_especie').on('change', function(){
    
    var selectValor = '#'+$(this).val();
    $('#racas').children('div').hide();
    $('#racas').children(selectValor).show();

  
  });
});
