var http = require('http');

var server = http.createServer( function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  var date = new Date();
  res.end('request url: ' + req.url + ', request methold: ' + req.method + ', date: ' + date);
});

server.listen(3000, '127.0.0.1');
