if (document.querySelectorAll('.nav-item').length >= 5) {
    let user_button = document.querySelectorAll('.nav-item')[1]
    let hid_menu = document.querySelector('.wrap')
    let cool_event = false

    user_button.addEventListener('mouseover', function() {
        hid_menu.style.display = 'block'
        cool_event = false
    })
    hid_menu.addEventListener('mouseover', function() {
        cool_event = false
        hid_menu.style.display = 'block'
    })
    hid_menu.addEventListener('mouseout', function() {
        cool_event = true
        setTimeout(function(){
            if (cool_event)
                hid_menu.style.display = 'none'
            cool_event = false
        }, 500)
    })
}