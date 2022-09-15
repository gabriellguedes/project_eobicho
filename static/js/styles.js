$(document).ready(function(){
  $('.mask-date').mask('00/00/0000');
  $('.dropdown-toggle').dropdown();
  
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

    // Desabilita o campo 'Saldo'
    $('#id_estoque-' + (count) + '-saldo').prop('type', 'hidden')

    // some animate to scroll to view our new form
    $('html, body').animate({
      scrollTop: $("#add-item").position().top - 200
    }, 800);

    $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
    $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');

    // Cria um span para mostrar o saldo na tela.
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px;"></span>')
    // Cria um campo com o estoque inicial.
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<input id="id_estoque-' + (count) + '-inicial" class="form-control" type="hidden" />')
    // Select2
    $('.clProduto').select2()
  });

