const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
app.use(cors());

const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: ["url1", "url2"],
    methods: ["GET", "POST"]
  }
});

let count = 0;

io.on('connection', (socket) => {
  count++;
  io.emit('count', count);

  socket.on('disconnect', () => {
    count = count > 0 ? count - 1 : 0;
    io.emit('count', count);
  });
});

app.get('/hello', (req, res) => {
  res.send('Hello, World!');
});

server.listen(3000, () => console.log('Server is running on port 3000'));
