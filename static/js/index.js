const hamburer = document.querySelector(".hamburger");
const navList = document.querySelector(".nav-list");
const navListClose = document.querySelector(".items-close-button")

if (hamburer) {
  hamburer.addEventListener("click", () => {
    navList.classList.toggle("open");
      navListClose.classList.toggle("appears");
  });
}

if (navListClose) {
  navListClose.addEventListener("click", ()=>{
    navList.classList.remove("open");
    navListClose.classList.remove("appears");
  })
}
// Popup
const popup = document.querySelector(".popup");
const closePopup = document.querySelector(".popup-close");

if (popup) {
  closePopup.addEventListener("click", () => {
    popup.classList.add("hide-popup");
  });

  window.addEventListener("load", () => {
    setTimeout(() => {
      popup.classList.remove("hide-popup");
    }, 1000);
  });
}

//Jquery code
//NavBar
$(()=>{
  $(window).on("scroll", ()=>{
   if ($(window).scrollTop() > 150) {
    $('.navigation').addClass('fixed');
    $('.profile-popup').addClass('profile-popup-scroll');
    $('.cartpopup').addClass('cartpopup-scrolled');
  } else {
    $('.navigation').removeClass('fixed');
    $('.profile-popup').removeClass('profile-popup-scroll');
    $('.cartpopup').removeClass('cartpopup-scrolled');
   }
  })
})

//Search PopUp
$(()=>{
  $('.search-icon').on('click', ()=>{
    $('.search-popup').addClass('search-popup-open');
  })
  $('.search-popup .exit').on('click', ()=>{
    $('.search-popup').removeClass('search-popup-open');
  })
})

//Profile Popup
$(()=>{
  $('.show-prof').on('click', function(){
    $('.profile-popup').slideToggle('show-profile');
  })
  $(window).on('scroll', function(){
    $('.profile-popup').fadeOut('show-profile');
  })
})


//Cart Popup
$(()=>{
  setTimeout(
    $('.initialbutton').on('click', function(){
      $('.cartpopup').slideDown();

      $(`.cartpopupexit span`).on('click', function(){
        $('.cartpopup').fadeOut();
      });
  }), 1000);
})

//Message Popup
$(()=>{
  $('.show-message-popup').on('click',function(e){
    e.preventDefault();
    console.log('working')
    $('.message-popup').css({'visibility':'visible','opacity':'1'});
    setTimeout(function(){
      $('.message-popup').css({'visibility':'hidden','opacity':'0'});
    }, 1500);
    $('.hide-message-popup').on('click', function(){
      $('.message-popup').css({'visibility':'hidden','opacity':'0'});
    })
  })
})

//Checkout Address Form
$(()=>{
  $('.another-address').on('click', function(){
    $('.payment .customer-form').slideToggle();
    if ($(this).children('button').text() == 'Cancel') {
      $(this).children('button').text('Add new address')
    } else {
      $(this).children('button').text('Cancel')
    }
  })
})

// Checkout Submit
$(()=>{
  let val =  $('input:radio[name=address]:checked').val();
  if ( !val) {
    $('.checkout-submit').attr('disabled', true);
    } else {
      $('.checkout-submit').attr('disabled', false)
    }
    $('input:radio[name=address]').on('click', function(){
      $('.checkout-submit').attr('disabled', false)
  })
})
