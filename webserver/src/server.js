const { join } = require('path')
const express = require('express')
const favicon = require('serve-favicon')
const app = express()
const PORT = 80
const {env} = require('process');

var container = env.EI_IMG;

app.use(favicon(join(__dirname, '..', 'views', 'public', 'favicon.ico')))
app.set('views', join(__dirname, '..', 'views', 'public'))
app.set('view engine', 'html')

// Enable the public directory for resource files
app.use('/public', express.static(
  join(__dirname, '..', 'views', 'public')
))

app.use('/storage', express.static(
  join(__dirname, '..', '..', '..', '..', 'app', 'storage')
))

// reply to request with the index file
app.get('/', function (req, res) {
  res.sendFile(join(__dirname, '..', 'views', 'index.html'))
})

// reply to script request in index file just to show EI_IMG on web page!
app.get("/data.js", function (req, res) {   
  res.send('window.SERVER_DATA={"con": "' + container + '"}');
});


// start a server on port 80 and log its start to our console
app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`)
})

