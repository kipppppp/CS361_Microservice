<h1>Fantasy Sports Microservice</h1>

<h2>Description</h2>
<p>
This project is a microservice that utilizes a websocket to facilitate information exchange between a javascript webapp and a NoSQL database. The microservice (written in python) returns JSON data with the overall score for the requested fantasy sports team. No specific request information is required at this point, but can be implemented if the function of the microservice expands to complete additional processes.
</p>

<h2>Languages Used</h2>
<ul>
  <li>Python</li>
  <li>JavaScript</li>
  <li>HTML</li>
</ul>

<h2>Python Packages Used</h2>
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

```js
const heading = document.getElementById('main-heading');
const button = document.getElementById('microservice-btn');

// Add event listener to the button
button.addEventListener('click', () => {
    const ws = new WebSocket("ws://127.0.0.1:65432/")

    // Check if the microservice is running
    ws.addEventListener("error", (event) => {
        heading.textContent = "Microservice not running.";
    });

    // No errors, retreive data and update web page
    ws.onmessage = function(event){
    heading.textContent = event.data;
    ws.close();
    }
});
```

<h3>Receiving</h3>
<p>
    In the above example, "heading" is an html header element. The "onmessage" function updates "heading" to display the JSON data received from the microservice.
</p>
<p>
    The nested event listener will display error information if the microservice is not running.
</p>

```js
    // Check if the microservice is running
    ws.addEventListener("error", (event) => {
        heading.textContent = "Microservice not running.";
    });
```

<p>
  The received JSON data can be reformatted and displayed however necessary.
</p>

<h2>Screenshots</h2>

<div align="center">
<h3>Before data request</h3>
<img src="https://imgur.com/eJWDMLy.png" alt="Before request"/>
<br/>
<br/>
<h3>After data request</h3>
<img src="https://imgur.com/qHx1seD.png" alt="Received data"/>
<br/>
<br/>
<h3>Microservice not running when request is made</h3>
<img src="https://imgur.com/49Ms40v.png" alt="Error, microservice not running"/>
<br/>
</div>

<h2>UML Diagram</h2>
<br/>
<img src="https://imgur.com/LlDrg2N.png" alt="UML diagram"/>
<br/>
