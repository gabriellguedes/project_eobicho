$(document).ready(function(){
  $('.mask-date').mask('00/00/0000');
  $('.mask-cpf').mask('000.000.000-00', {reverse: true});
  $('.mask-tel').mask('(00) 00000-0000');
  $('.mask-peso').mask('00.000', {reverse: true});
  $('.mask-cep').mask('00000-000');

  $('.dropdown-toggle').dropdown();
  
 
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
  var $input_pet   = document.getElementById('id_photo'),
     $fileName = document.getElementById('file-name');

  $input_pet.addEventListener('change', function(){
  $fileName.textContent = this.value;
  });
  

});


$('#showpassword').click(function mostrarSenha(){
    var tipo = document.getElementById("id_password");
    var icon = document.getElementById("icon_show_password")
    if(tipo.type == "password"){
        tipo.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    }else{
        tipo.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
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

    
jQuery(document).ready(function(){

    var btn = 'form[name=form_cadastro] button[name=btn_criar_conta]';      /*INFORME O SELETOR DO BOTÃO*/
    var checkbox = '#check_termos';  /*INFORME O NOME DO ID DO CHECKBOX*/
    
    jQuery(btn).attr('disabled', 'disabled').css("opacity", "0.6");
   
    jQuery(checkbox).click(function(){
      
        if(jQuery(this).is(':checked')){
            
            jQuery(btn).removeAttr('disabled').css("opacity", "1");
        
        }else{
            
            jQuery(btn).attr('disabled', 'disabled').css("opacity", "0.6");
            
        }
        
    });
});

jQuery(document).ready(function(){

    var btn = 'form[name=FormPermissionTutor] button[name=BtnPermissionTutor]';      /*INFORME O SELETOR DO BOTÃO*/
    var checkbox = '#permission_banho_tosa';  /*INFORME O NOME DO ID DO CHECKBOX*/
    
    jQuery(btn).attr('disabled', 'disabled').css("opacity", "0.6");
   
    jQuery(checkbox).click(function(){
      
        if(jQuery(this).is(':checked')){
            
            jQuery(btn).removeAttr('disabled').css("opacity", "1");
        
        }else{
            
            jQuery(btn).attr('disabled', 'disabled').css("opacity", "0.6");
            
        }
        
    });
});

