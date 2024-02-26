<h1>Fantasy Sports Microservice</h1>

<h2>Description</h2>
This project implements a websocket microservice that facilitates a transaction between a javascript webapp and NoSQL database. The webapp (written in python) returns JSON data related to the request. The current version returns sample player data, and is
designed for one task. No specific request information is required at this point, but can be implemented if the function of the microservice expands to complete additional processes.
<br />

<h2>Languages Used</h2>
<ul>
  <li>Python</li>
  <li>JavaScript</li>
  <li>HTML</li>
</ul>

<h2>Packages Used</h2>
<ul>
  <li>asyncio</li>
  <li>Websockets</li>
  <li>JSON</li>
</ul>

<h2>Example JS Call</h2>
<p>
  In the code block below, "button" is an html button element. This event listener creates a websocket to read data sent from the localhost (127.0.0.1) at the specified port (65432).
  The "onmessage" function below updates "heading", which is an html header element in this case. The text in "heading" is replaced by the received JSON data.
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

<h2>Screenshots</h2>

<p align="center">
Before data request. <br/>
<img src="https://imgur.com/YEU6U8J.png" alt="Before request"/>
<br />
<br />
After data request.
<br/>
<img src="https://imgur.com/2pWZi5H.png" alt="Enter desired move"/>
<br />

<h2>UML Diagram</h2>
<br/>
<img src="https://imgur.com/4fVJQYm.png" alt="Before request"/>
<br />
