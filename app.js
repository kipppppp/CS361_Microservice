const heading = document.getElementById('main-heading');
const button = document.getElementById('microservice-btn');


// Add event listener to the button
button.addEventListener('click', () => {
    const ws = new WebSocket("ws://127.0.0.1:65432/")
    heading.textContent = "Server not running.";

    ws.onmessage = function(event){
        heading.textContent = event.data;
        ws.close();
    };
    
});
