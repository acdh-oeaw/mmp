(function set_form_attributes() {
    var textinput = document.getElementsByClassName('textinput');
    for (var i = 0; i < textinput.length; i++) {
        textinput[i].classList.add('form-control');
    }
    var select = document.getElementsByClassName('select');
    for (var i = 0; i < select.length; i++) {
        select[i].classList.add('custom-select');
    }
})();        