const express = require("express");

const server = express();

server.all("/", (req, res) => {
    res.send("Hello. I am alive!")
})

function keep_alive() {
    server.listen(process.env.PORT || 3000, () => { console.log("Server is Ready!") });
}

module.exports = keep_alive;

// const keep_alive = require('./keep_alive');
// keep_alive();
