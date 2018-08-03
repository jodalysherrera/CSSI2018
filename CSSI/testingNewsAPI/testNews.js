
//url is hardcoded for ABC News and 'climate'
//need to add {}
//need to print articles on page
//input=q then on click print results
//need for loop?
var url = 'https://newsapi.org/v2/everything?sources=abc-news&q=climate&apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'


var req = new Request(url);

fetch(req)
    .then(function(response) {
        console.log(response.json());
    })


    //
    // function createArticle(url){
    //   let image= document.createElement('art');
    //   article.src = url;
    //   document.body.appendChild(article);
    // }
    //
    // let go = document.querySelector('#go');
    // let input =document.querySelector('#q');
    //
    // go.addEventListener('click', e=>{
    //   let q = input.value;
    //   fetch(q);
    // })



// print('articles'+response.json())

// //All named sources available
// 'https://newsapi.org/v2/sources?apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'
// //All articles about #
// 'https://newsapi.org/v2/everything?q=#&apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'
// //from a source
// 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'
//
//
// 'https://newsapi.org/v2/everything?q=immigration?sources=abc_news&apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'
