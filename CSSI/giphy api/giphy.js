//make form for searching
//**get results for a search term
//display gifs

const apiKey = 'm1P8ktlavJHyID5Njnj0MLC7X8kkk0hh';


let url= 'http://api.giphy.com/v1/gifs/search';


function fetchGif(searchTerm){
  let query = `${url}?api_key=${apiKey}&q=${searchTerm}&limit=1`;
  console.log(searchTerm);
  window.fetch(query).then(data =>{
    return data.json();
  }).then(json => {
    let results =json.data;
    console.log(json.data);
    let result=results[0];
    let imageUrl= result.images.downsized.url;
    createImage(imageUrl);
    console.log(result);
  })
}


function createImage(url){
  let image= document.createElement('img');
  image.src = url;
  document.body.appendChild(image);
}

let go = document.querySelector('#go');
let input =document.querySelector('#q');

go.addEventListener('click', e=>{
  let q = input.value;
  fetchGif(q);
})

//fetchGif('dog');
