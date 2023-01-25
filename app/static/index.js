let ws = new WebSocket("ws://localhost:8000/ws");
//let array = new JSON //array = [{1:'string', 2:"string"}]
let array = [];
var counter = 1;
app = document.getElementById("app")
ws.onmessage = function(event) {
    if (true){counter++;};
    let messages = document.getElementById('messages')
    array.push(event.data)
};

function sendMessage(event) {
    let input = document.getElementById("messagePost")
    let view = JSON.stringify({id: counter, data: input.value})
    ws.send(view)
    input.value = ''
    event.preventDefault()
}
function home(){
    app.innerHTML = '<form action="" onsubmit="sendMessage(event)"><input type="text" id="messagePost" autocomplete="off"/><button>Send</button></form><ul id="messages"></ul>'
}
function show(){
    app.innerHTML = array
}