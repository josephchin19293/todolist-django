$(function() {

  let degree = 90;

  // Rotates '+' and drops down or recloses input box on click
  $('.fa-plus').on('click', function() {
    if (degree === 135) {
      degree = 45;
    }
    // Sets CSS transform properties. Selector 'this' refers to '+' (with class '.fa-plus') being clicked
    $(this).css({
      '-webkit-transform': 'rotate(' + degree + 'deg)',
      '-moz-transform': 'rotate(' + degree + 'deg)',
      '-ms-transform': 'rotate(' + degree + 'deg)',
      '-o-transform': 'rotate(' + degree + 'deg)',
      'transform': 'rotate(' + degree + 'deg)',
      'transition': '0.2s linear'
    });
    degree += 45;
    // Animates opacity of text box, setting its display style property to none once its opacity reaches 0 if it's visible, or the inverse if already hidden
    $('input[type="text"]').fadeToggle();
    $('input[type="submit"]').fadeToggle();
    $('form').fadeToggle();
  });

  // Upon clicking on list items, adds to class 'completed' (CSS adds strike-through for class)
  $('ul').on('click', 'li', function() {
    $(this).toggleClass('completed');
  });


  // Enables drag reordering of list items (uses linked jQuery UI library)
  $('.sortable').sortable();

});
