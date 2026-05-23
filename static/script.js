async function checkPassword(){

const password=
document.getElementById(
"password"
).value;

const response=
await fetch('/check',{

method:'POST',

headers:{
'Content-Type':
'application/json'
},

body:JSON.stringify({
password:password
})

});

const data=
await response.json();

let percentage=
(data.score/8)*100;

document.getElementById(
"score"
).innerHTML=
Math.round(
percentage
)+"%";

document.getElementById(
"strengthText"
).innerHTML=
data.strength;

let suggestions="";

data.suggestions
.forEach(item=>{

suggestions+=
`<p>✓ ${item}</p>`;

});

document.getElementById(
"suggestions"
).innerHTML=
suggestions;

}