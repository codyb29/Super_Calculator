/* obtain from: https://stackoverflow.com/questions/16308779/how-can-i-hide-show-a-div-when-a-button-is-clicked#16308830 */
function showhide(id) {
    var n = document.getElementsByTagName('input')[1].value;
    if (n > -1 && n < 100001) {
        var e = document.getElementById(id);
        e.style.display = (e.style.display == 'block') ? 'none' : 'block';
    }
}
