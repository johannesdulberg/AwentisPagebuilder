/*!
* Start Bootstrap - Creative v7.0.4 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

});



let controller = new ScrollMagic.Controller();
let timeline = new TimelineMax();

timeline
    .to('.parallaxMoveable0',3,{y: -500})
    .to('.parallaxMoveable',3,{y: -500},"-=3")
    .to('.parallaxMoveable1',3,{y: -400},"-=3")
    .to('.parallaxMoveable2',3,{y: -300},"-=3")
    .to('.parallaxMoveable3',3,{y: -200},"-=3")
    .to('.parallaxBackground',3,{y: -100},"-=3")
    .to('.parallaxTitle',3,{y: -300},"-=3")
    .to('.parallaxContent',3,{y: -1000},"-=3")

let scene = new ScrollMagic.Scene({
    triggerElement :"section",
    duration:"100%",
    triggerHook:0,
})
    .setTween(timeline)
    .addTo(controller);

let controller2 = new ScrollMagic.Controller();
let timeline2 = new TimelineMax();
    
    timeline2
        .to('.ParallaxBild',3,{y: 1000})
    
    let scene2 = new ScrollMagic.Scene({
        triggerElement :"summary",
        duration:"1000%",
        triggerHook:1,
    })
        .setTween(timeline2)
        .addTo(controller2);

