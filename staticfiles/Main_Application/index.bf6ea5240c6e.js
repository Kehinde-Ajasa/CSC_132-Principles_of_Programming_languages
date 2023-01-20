document.addEventListener('DOMContentLoaded',function(){
    // displaying both left and right part of the hero section once the page loads
    document.querySelector('.hero_left').classList.add('reveal_hero')
    document.querySelector('.hero_right').classList.add('reveal_hero')

    // reveal projects with a smooth transition when scrolled to where they are positioned
    window.addEventListener('scroll',revealProjects)

    function revealProjects(){
        document.querySelectorAll('.project').forEach(function(section){
            var windowheight = window.innerHeight
            var revealtop = section.getBoundingClientRect().top
            var reavealpoint = 0
            if (revealtop < windowheight - reavealpoint){
                section.classList.add('reveal_projects')
            }
            else{
                section.classList.remove('reveal_projects')
            }
        })
    }

    function clear(){
        var confirmation_txt = document.querySelector('.confirmation_text')
        confirmation_txt.innerHTML = ""
    }

    document.querySelector('#submit_btn').addEventListener('click',function(){

        var name = document.querySelector('#username')
        var email = document.querySelector('#useremail')
        var confirmation = document.querySelector('.confirmation_text')
        if (email.value !== "" && name.value !== ""){

            if(email.value.includes('@')){
                fetch('/save_user',{
                    method : 'POST',
                    body : JSON.stringify({
                        Name :name.value,
                        Email : email.value
                    })
                })
            
                .then(response => response.json())
                .then(data => {
                    name.value = ""
                    email.value = ""
                    confirmation.innerHTML = 'Thank you, your email has been received. A confirmation email will be sent to you soon '
                    confirmation.style.color = '#7000FF'
                    setTimeout(clear,4000)
                    
                })
            
            }
            else{
                confirmation.innerHTML = 'Email address must include @'
                confirmation.style.color = 'red'
                setTimeout(clear,4000)
            }
        }
        else{
            confirmation.innerHTML = 'Enter full details'
            confirmation.style.color = 'red'
            setTimeout(clear,4000)
        }

    })

})