const express = require('express');
const db = require('./database');

const app = express();
app.use(express.json());
app.listen(3001, () => console.log("Servidor rodando na porta 3001"));

// CRIAR Curso (POST)
app.post("/cursos", (req, res) => {
    const novoCurso = req.body;
    const campusCode = novoCurso.id_campus.toString().padStart(2, '0');
    const cursoCode = `1${novoCurso.turno}10${campusCode}`;
    novoCurso.id = parseInt(cursoCode);
    db.cursos.push(novoCurso);
    res.send("Curso adicionado com sucesso!");
});

// LER TUDO Cursos (GET)
app.get("/cursos", (req, res) => {
    res.json(db.cursos);
});

// LER 1 Curso (GET)
app.get("/cursos/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const curso = db.cursos.find(curso => curso.id === cursoId);
    if (curso) {
        res.json(curso);
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

// ALTERAR Curso (PUT)
app.put("/cursos/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const updatedCurso = req.body;
    const index = db.cursos.findIndex(curso => curso.id === cursoId);
    if (index !== -1) {
        db.cursos[index] = updatedCurso;
        res.send("Curso atualizado com sucesso!");
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

// APAGAR Curso (DELETE)
app.delete("/cursos/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const index = db.cursos.findIndex(curso => curso.id === cursoId);
    if (index !== -1) {
        db.cursos.splice(index, 1);
        res.send("Curso removido com sucesso!");
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

// -----------------------------------------------------------------------------------------------

// CRIAR CCR (POST)
app.post("/ccrs", (req, res) => {
    const novoCCR = req.body;
    db.ccrs.push(novoCCR);
    res.send("CCR adicionado com sucesso!");
});

// LER TUDO CCRs (GET)
app.get("/ccrs", (req, res) => {
    res.json(db.ccrs);
});

// LER 1 CCR (GET)
app.get("/ccrs/:id", (req, res) => {
    const ccrId = req.params.id;
    const ccr = db.ccrs.find(ccr => ccr.id === ccrId);
    if (ccr) {
        res.json(ccr);
    } else {
        res.status(404).send("CCR não encontrado.");
    }
});

// ALTERAR CCR (PUT)
app.put("/ccrs/:id", (req, res) => {
    const ccrId = req.params.id;
    const updatedCCR = req.body;
    const index = db.ccrs.findIndex(ccr => ccr.id === ccrId);
    if (index !== -1) {
        db.ccrs[index] = updatedCCR;
        res.send("CCR atualizado com sucesso!");
    } else {
        res.status(404).send("CCR não encontrado.");
    }
});

// APAGAR CCR (DELETE)
app.delete("/ccrs/:id", (req, res) => {
    const ccrId = req.params.id;
    const index = db.ccrs.findIndex(ccr => ccr.id === ccrId);
    if (index !== -1) {
        db.ccrs.splice(index, 1);
        res.send("CCR removido com sucesso!");
    } else {
        res.status(404).send("CCR não encontrado.");
    }
});