const express = require('express');
const cursosController = require('./controllers/cursosController');
const ccrsController = require('./controllers/ccrsController');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'views')));
app.use(express.static('public'));
app.use('/cursos', cursosController);
app.use('/ccrs', ccrsController);
app.listen(3001, () => console.log("Servidor rodando na porta 3001"));

app.get("/index", (req, res) => {
    const filePath = path.join(__dirname, 'views', 'index.html');
    res.sendFile(filePath);
});