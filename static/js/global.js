$(() => {
  // --------------------------------------------------
  // --------------------- [ Trending Carouse l -------
  // --------------------------------------------------
  $(".autoplay").slick({
    // slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    dots: true,
    infinite: true,
    speed: 300,
    pauseOnHover: true,
    slidesToShow: 4,
    slidesToScroll: 4,
    arrows: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  const incrementItemQuantity = (event) => {
    let newValue = quantityInput.value;
    quantityInput.value = newValue++;
    console.log("🚀 ~ file: global.js ~ line 48 ~ incrementItemQuantity ~  newValue++",  newValue++)
  };
  const decrementItemQuantity = (event) => {
    let newValue = quantityInput.value;
    if (newValue === 1) return;
    quantityInput.value = newValue--;
    console.log("🚀 ~ file: global.js ~ line 53 ~ decrementItemQuantity ~ newValue--", newValue--)
  };

  let quantityInput = document.querySelector("#quantity-field");
  document.querySelector("#addBtn").addEventListener('click', incrementItemQuantity)
  document.querySelector("#minusBtn").addEventListener('click', decrementItemQuantity)
});
