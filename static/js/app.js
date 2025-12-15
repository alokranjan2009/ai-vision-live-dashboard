function awaken() {
  document.getElementById("state").innerText = "STATE: AWAKENED";
  document.getElementById("player").src = "static/videos/awakening.mp4";
}

function resetMatrix() {
  document.getElementById("state").innerText = "STATE: RESETTING";
  document.getElementById("player").src = "static/videos/matrix_reset.mp4";
}
