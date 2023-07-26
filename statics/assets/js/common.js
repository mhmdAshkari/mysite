/*$(document).ready(function (){

});*/

function toastMSG(msg, color) {
    M.toast({html: '<span class="toast-text center">'+msg+'</span>', displayLength: 5000, classes: ''+color+''});
}

function random_int(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}
