// Inicializar o Select do Materialize

$(document).ready(() => {
    $('select').formSelect();
});

$(document).ready(() => { 
    let $cpf = $("#id_cpf");
    $cpf.mask('000.000.000-00', { reverse: false });
});

// AJAX para busca de visitantes

$(document).ready(() => {
    $('#search').keyup(() => {
        $('#result').html('');

        let searchField = $('#search').val();
        let expression = new RegExp(searchField, "i");

        let found = false;

        if(searchField.length !== 0){
            document.getElementById('itensBusca').innerHTML = '<ul id="result" class="lista-results"></ul>';
        }
        else{
            document.getElementById('itensBusca').innerHTML = '';
        }

        $.getJSON('http://127.0.0.1:8000/api/pessoas/', (data) => {
            let count = 0;

            $.each(data, (key, value) => {
                if(count == 5){
                    return false;
                }

                if(value.fields.nome.search(expression) != -1 || value.fields.cpf.search(expression) != -1){
                    if(count === 0){
                        $('#result').append(`<li value='${ value.pk }' onClick='selecionarVisitante(this);'><div class='firstItem'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                        found = true;
                    }
                    else{
                        $('#result').append(`<li value='${ value.pk }' onClick='selecionarVisitante(this);'><div class='itemListaBusca'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                    }

                    count++;
                }
            });

            if(!found){
                $('#result').append(`<li onClick='fecharBox();'><div class='firstItem'>Nenhum registro encontrado.</div></li>`);
            }
        });
    });
});

function selecionarVisitante(elem){
    document.getElementById('itensBusca').innerHTML = '';
    document.getElementById('id_pessoa').value = elem.value;
    document.getElementById('search').value = elem.textContent;
}

function fecharBox(){
    document.getElementById('itensBusca').innerHTML = '';
    document.getElementById('search').value = '';
}

// Ocultar seta de retorno

$(document).ready(() => {
    $('body').bind('mousewheel', function(e){
        if(e.originalEvent.wheelDelta /120 > 0) {
            console.log('scrolling up !');
        }
        else{
            console.log('scrolling down !');
        }
    });
});

