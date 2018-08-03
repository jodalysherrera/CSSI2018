console.log('hello');
let name= "jess";
let daysleft=14;

console.log("hello," + name);
console.log("there are " + daysleft + " days left in CSSI");

if (daysleft<6){
  console.log('goodluck on final project');
}

if (daysleft<6 && name=="matthew"){
  console.log('help with projects');
}
//both conditions have to be true^
//||=or
if (name =='ciera' || name=='matthew'|| name=='rachel'){
  console.log('youre an insturctor');
} else if  (name=='logan'||name=="sharon"||name=='stephanie'){
    console.log('youre a TA')
}else if (name=='jess'||name=="julia"){
    console.log('youre a sitelead')
}else {
    console.log('youre a student');
}
