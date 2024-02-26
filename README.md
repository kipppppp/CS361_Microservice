<h1>Fantasy Sports Microservice</h1>

<h2>Description</h2>
This project implements a websocket microservice that facilitates a transaction between a javascript webapp and NoSQL database. The webapp (written in python) returns JSON data related to the request. The current version returns sample player data.
<br />

<h2>Languages Used</h2>
- <b>Python</b>
- <b>JavaScript</b>
- <b>HTML</b>

<h2>Packages Used</h2>
- <b>Websockets</b>
- <b>asnycio</b>
- <b>JSON</b>

<h2>Example JS Call</h2>
<p>
  In the code block below, "button" is an html button element. This event listener creates a websocket to read data sent from the localhost (127.0.0.1) at the specified port (65432).
  The call below updates "heading", which is an html header element in this case. The text in "heading" is replaced by the received JSON data.
</p>
<code>button.addEventListener('click', () => {
    const ws = new WebSocket("ws://127.0.0.1:65432/")
    ws.onmessage = function(event){
        heading.textContent = event.data;
        ws.close();
    };
</code>
<br />
<p>
  The received data can be reformatted and displayed however necessary.
</p>
