document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("button").onclick = count;
});

let value=0;
function count(){
    value++;
    document.querySelector("#blabla").innerHTML = value;

    if (value % 10 === 0) {
        alert(`You have reached counter value ${value}`);
    }
}
