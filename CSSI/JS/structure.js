
let scores = [97,92,90,87,88,100,99,105];
let max = scores [0];

for (let i=0; i< scores.length; i++){
  if(scores[i]>max){
    max=scores[i];
  }
}

//console.log('the max score is ' + max);

let total= 0;

for (let i=0; i< scores.length; i++){
  total+= scores[i];
}

//console.log(total);

let names = ['savion', 'jenny', 'olivia', 'joshua'];
names.forEach(name => {
//  console.log('welcome' + name)
}
)

//let matthew = ['matthew','levine'.'darthmouth','harry potter'];
//let yojairo = ['yojairo','morales','usc','kendrick lamar'];

let matthew = {
  'firstName':'matthew',
  'lastName':'levine',
  'university': 'darthmouth',
  'culture':'harry potter',
  'siblings':4,
};

console.log(matthew.siblings);

let yojairo= {
  'firstName':'yojairo',
  'lastName':'morales',
  'university': 'usc',
  'culture':'kendrick lamar',
};


let people= [matthew, yojairo];
people.forEach(person =>{
  console.log(person.firstName + ' really likes ' +person.culture)

})

let style = {
  'backgroundColor':'',
}
