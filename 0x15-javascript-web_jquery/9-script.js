$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
  if (status == 'success') {
    $('#hello').html(data.hello);
  }
});