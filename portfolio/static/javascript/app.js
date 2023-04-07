const hamburger = document.querySelector('.hamburger')
const hamburger2 = document.querySelector('.hamburger2')
const nav = document.querySelector('.submenu_cover')
const link_title = document.querySelector('.link_title')
const child_nav = document.querySelectorAll('.child_nav a')


// function to display the title of the navigaion link
const showTitle = ()=>{
    for (let i=0; i< child_nav.length; i++){
        child_nav[i].addEventListener('mouseover', (e)=>{
            e.preventDefault()
            link_title.classList.add('link_title_active')
            link_title.innerHTML = child_nav[i].innerHTML
        })
        child_nav[i].addEventListener('mouseout', (e)=>{
            e.preventDefault()
            link_title.classList.remove('link_title_active')
        })
        
    }
}
showTitle()

// This function displays the navigation links
const display_nav = ()=>{
    hamburger.addEventListener('click', ()=>{
        nav.classList.add('active')
    })
    hamburger2.addEventListener('click', ()=>{
        nav.classList.remove('active')
    })
}
display_nav()

// rotate hamburger svg icon
function rotate_svg(){
    hamburger2.addEventListener('mouseover', ()=>{
        hamburger2.classList.add('rotate_svg')
    })
    hamburger2.addEventListener('mouseout', ()=>{
        hamburger2.classList.remove('rotate_svg')
    })
}
rotate_svg()

