$(document).ready(function(){
  $('.mask-date').mask('00/00/0000');
  $('.mask-cpf').mask('000.000.000-00', {reverse: true});
  $('.mask-tel').mask('(00) 00000-0000');
  $('.dropdown-toggle').dropdown();
  
  // Oculta as opções do segundo select:
    $("#t-shift option").hide();
    
    // Observa o evento change do primeiro select:
    $("#p-shift").on("change", function () {
    
      // Recupera o valor selecionado:
      let course = $("#p-shift").val();
      
      // Oculta as opções atuais:
      $("#t-shift option").hide();
      
      // Exibe as opções conforme a seleção:
      $("#t-shift option[data-course="+ course +"]").show();
    
    });

  $('#id_especie').on('change', function(){
    
    var selectValor = '#'+$(this).val();
    $('#racas').children('div').hide();
    $('#racas').children(selectValor).show();

  
  });
});
$('#add-item').click(function(ev) {
    ev.preventDefault();
    var count = $('#estoque').children().length;
    var tmplMarkup = $('#item-estoque').html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $('div#estoque').append(compiledTmpl);

    // update form count
    $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

    // some animate to scroll to view our new form
    $('html, body').animate({
      scrollTop: $("#add-item").position().top - 200
    }, 800);

    
  });

