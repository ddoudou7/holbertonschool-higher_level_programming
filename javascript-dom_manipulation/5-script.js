document.addEventListener('DOMContentLoaded', function () {
  const div = document.querySelector('#toggle_class');
  const button = document.querySelector('#toggle_button');

  button.addEventListener('click', function () {
    div.classList.toggle('red');
  });
});
