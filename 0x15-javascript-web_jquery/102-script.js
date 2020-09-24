$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: url,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
