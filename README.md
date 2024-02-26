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

<h2>Requesting/Receiving Data</h2>
<p>
  The code block below creates a websocket to read data sent from the localhost (127.0.0.1) at the specified port (65432). In this example, "button" is an html button element. 
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
<p>
NOTE: There are currently no functions defined within the microservice beyond creating the websocket. This will change during integration (next sprint), when data processing parameters/queries are defined and implemented.
</p>
<p>
The following: "process request", "Query for desired data set/Return desired data set", and "JSON-ify data" will all become functions when integrated.
</p>
<br/>
<img src="https://imgur.com/4fVJQYm.png" alt="Before request"/>
<br />
