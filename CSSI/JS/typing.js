let box=document.querySelector('#box');
let boxes= document.querySelectorAll('div');
console.log(boxes);

boxes.forEach(box => {
  box.addEventListener('mouseenter', e=> {
    box.classList.add('spin');

  });

  box.addEventListener('mouseleave' , e => {
    box.classList.remove('spin');
  })
})
window.addEventListener('keydown', e=> {
  if (e.key == 'g' || e.key == 'G'){
      boxes.forEach(box => {
        box.classList.remove('red');
        box.classList.add('green');
      })
  }
})
