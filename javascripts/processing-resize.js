var ProcessingInit = function() {
  function resizeWindow() {
    var pCanvas = Processing.getInstanceById('pCanvas');
    pCanvas.resize($(window).width(),$(window).height());
  }
  
  $(window).resize(resizeWindow);
  resizeWindow();
}