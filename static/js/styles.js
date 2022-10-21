$(document).ready(function(){
  $('.mask-date').mask('00/00/0000');
  $('.mask-cpf').mask('000.000.000-00', {reverse: true});
  $('.mask-tel').mask('(00) 00000-0000');
  $('.mask-peso').mask('00.000', {reverse: true});
  $('.mask-cep').mask('00.000-000');

  $('.dropdown-toggle').dropdown();
  
  $("#id_endereco_set-0-cep").blur(function(){
        // Remove tudo o que não é número para fazer a pesquisa
        var cep = this.value.replace(/[^0-9]/, "");
        
        // Validação do CEP; caso o CEP não possua 8 números, então cancela
        // a consulta
        if(cep.length != 8){
          return false;
        }
        
        // A url de pesquisa consiste no endereço do webservice + o cep que
        // o usuário informou + o tipo de retorno desejado (entre "json",
        // "jsonp", "xml", "piped" ou "querty")
        var url = "https://viacep.com.br/ws/"+cep+"/json/";
        
        // Faz a pesquisa do CEP, tratando o retorno com try/catch para que
        // caso ocorra algum erro (o cep pode não existir, por exemplo) a
        // usabilidade não seja afetada, assim o usuário pode continuar//
        // preenchendo os campos normalmente
        $.getJSON(url, function(dadosRetorno){
          try{
            // Preenche os campos de acordo com o retorno da pesquisa
            $("#id_endereco_set-0-Endereço").val(dadosRetorno.logradouro);
            $("#id_endereco_set-0-bairro").val(dadosRetorno.bairro);
            $("#id_endereco_set-0-cidade").val(dadosRetorno.localidade);
            $("#id_endereco_set-0-uf").val(dadosRetorno.uf);
          }catch(ex){}
        });
      });

  $('#id_especie').change(function(){
      const url = $('#FormAddPet').attr("data-funcoes-url");
      especieId =  $(this).val();
      $.ajax({
        url : url,
        data : { 'id_especie': especieId},
        success: function(data){
          $("#id_raca").html(data);
        }
      });

    });
  
  $('#id_pet_set-0-especie').change(function(){
      const url = $('#FormAddPetCliente').attr("data-funcoes-url");
      especieId =  $(this).val();
      $.ajax({
        url : url,
        data : { 'id_pet_set-0-especie': especieId},
        success: function(data){
          $("#id_pet_set-0-raca").html(data);
        }
      });

    });

  $('#id_especie').change(function(){
      const url = $('#FormUpdatePet').attr("data-funcoes-url");
      especieId =  $(this).val();
      $.ajax({
        url : url,
        data : { 'id_especie': especieId},
        success: function(data){
          $("#id_raca").html(data);
        }
      });

    });

  $('#id_especie').change(function(){
      const url = $('#FormUpdatePet').attr("data-funcoes-url");
      especieId =  $(this).val();
      $.ajax({
        url : url,
        data : { 'id_especie': especieId},
        success: function(data){
          $("#id_raca").html(data);
        }
      });

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

$('#add-doenca').click(function(ev) {
    ev.preventDefault();
    var count = $('#f_doenca').children().length;
    var tmplMarkup = $('#item-doenca').html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $('div#f_doenca').append(compiledTmpl);

    // update form count
    $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

    // some animate to scroll to view our new form
    $('html, body').animate({
      scrollTop: $("#add-doenca").position().top - 200
    }, 800);
});
