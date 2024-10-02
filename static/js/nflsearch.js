document.getElementById('submit-button').addEventListener('click', function () {
  let player_name = document.getElementById('player').value
  let position = document.getElementById('position').value
  let stat = document.getElementById('stat').value

  window.location.href = 'visualize/?player=' + encodeURIComponent(player_name) +
      '&position=' +encodeURIComponent(position) +
      '&stat=' + encodeURIComponent(stat)
});