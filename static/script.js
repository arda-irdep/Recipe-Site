function Search() {
    var input, filter, divs, a, i, txtValue;
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    divs = document.getElementsByClassName('recipe');
    
    for (i = 0; i < divs.length; i++) {
        
        a = divs[i].getElementsByTagName('a')[0];
        txtValue = a.textContent || a.innerText;

        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            divs[i].style.display = '';
        }
        
        else {
            divs[i].style.display = 'none';
        }
    }
}