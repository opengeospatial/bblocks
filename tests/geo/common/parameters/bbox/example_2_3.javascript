bbox = [-124.7844079,24.7433195,-66.9513812,49.3457868];

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?';

fetch(url + `bbox=${bbox.join(',')}`)
  .then((response) => response.json())
  .then((json) => console.log(json));