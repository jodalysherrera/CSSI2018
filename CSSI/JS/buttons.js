console.log('hello')
let likeButton = document.querySelector('#like');
console.log(likeButton);
likeButton.addEventListener( 'click', e => {
  likeButton.innerText='liked';
  likeButton.disabled= true;
});

let growButton = document.querySelector('#grow');
growButton.addEventListener('click', e => {
  console.log('click');
  let currentSize= growButton.style.fontSize;
  let newSize = parseInt(currentSize) + 10 ;
  console.log(currentSize);
  growButton.style.fontSize= newSize + 'px';
})
