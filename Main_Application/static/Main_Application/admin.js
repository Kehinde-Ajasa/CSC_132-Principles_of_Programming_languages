document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('.container').style.display = 'none'
    const password = prompt('Enter Password')
    if (password === 'code_admin'){
        document.querySelector('.container').style.display = 'block'
    }
    else{
        window.location.href = '/'
    }
})