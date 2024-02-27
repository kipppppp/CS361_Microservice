<h1>Fantasy Sports Microservice</h1>

<h2>Description</h2>
<p>
This project implements a websocket microservice that facilitates a transaction between a javascript webapp and NoSQL database. The microservice (written in python) returns JSON data related to the request. The current version returns sample player data, and is
designed for one task. No specific request information is required at this point, but can be implemented if the function of the microservice expands to complete additional processes.
</p>

<h3>To use the microservice with test data:</h3>
<p>
<ol>
  <li>Run microservice.py</li>
  <li>Open index.html in a browser window</li>
  <li>Select the "Request" button</li>
</ol>
</p>

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
<h3>Requesting</h3>
<p>
  The code block below creates a websocket to request/read data sent from the localhost (127.0.0.1) at the specified port (65432). In this example, "button" is an html button element.
  When the button is selected, a request is made.
</p>
<code>button.addEventListener('click', () => {
    const ws = new WebSocket("ws://127.0.0.1:65432/")
    ws.onmessage = function(event){
        heading.textContent = event.data;
        ws.close();
    };
</code>
<h3>Receiving</h3>
<p>
    In the above example, "heading" is an html header element. The "onmessage" function updates "heading" to display the JSON data received from the microservice.
</p>
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
NOTE: There are currently no functions defined within the microservice beyond creating the websocket. This will change during integration (next sprint), when data processing parameters/queries are implemented.
</p>
<p>
The following: "process request", "Query for desired data set/Return desired data set", and "JSON-ify data" will all become functions when integrated.
</p>
<br/>
<img src="https://imgur.com/4fVJQYm.png" alt="Before request"/>
<br />
