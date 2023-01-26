let ws = new WebSocket("ws://localhost:8000/ws");
let array = [];
app = document.getElementById("app")
ws.onmessage = function(event) {
    message = JSON.parse(event.data)
    array.push(message)
    textMassive = ''
    for(let i=0;i<array.length;i++){
        temp = JSON.parse(array[i])
        id = temp['id']
        data = temp['data']
        text = `<p>${id}.  ${data}</p><br/>`
        textMassive = textMassive + text
    }
    app.innerHTML = textMassive

};

function sendMessage(event) {
    let input = document.getElementById("messagePost")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()    
}