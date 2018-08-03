let rightButton= document.querySelector('#right');
rightButton.addEventListener('click',e =>{
  let box=document.querySelector('#box');
  let currentleft=box.style.left;
  console.log(currentleft);
  let newleft= parseInt(currentleft)+10;
  box.style.left=newleft + 'px';
})

let leftButton= document.querySelector('#left');
leftButton.addEventListener('click',e =>{
  let box=document.querySelector('#box');
  let currentright=box.style.left;
  console.log(currentright);
  let newright = parseInt(currentright)-10;
  box.style.left=newright + 'px';
})

let upButton= document.querySelector('#up');
upButton.addEventListener('click',e =>{
  let box=document.querySelector('#box');
  let currentdown=box.style.top;
  console.log(currentdown);
  let newdown = parseInt(currentdown)-10;
  box.style.top=newdown + 'px';
})

let downButton= document.querySelector('#down');
downButton.addEventListener('click',e =>{
  let box=document.querySelector('#box');
  let currentup=box.style.top;
  console.log(currentup);
  let newup = parseInt(currentup)+10;
  box.style.top=newup + 'px';
})
