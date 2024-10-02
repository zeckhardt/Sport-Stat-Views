document.getElementById('submit-button').addEventListener('click', function () {
    let player_name = document.getElementById('player').value
    let stat = document.getElementById('stat').value
    let range = document.getElementById('range').value

    window.location.href = 'visualize/?player=' + encodeURIComponent(player_name) +
        '&stat=' + encodeURIComponent(stat) +
        '&range=' + encodeURIComponent(range);
})