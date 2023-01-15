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

})