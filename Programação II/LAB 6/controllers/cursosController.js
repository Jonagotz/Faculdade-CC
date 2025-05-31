const express = require('express');
const db = require('../models/database');
const router = express.Router();

// CRIAR Curso (POST)
router.post("/", (req, res) => {
    const novoCurso = req.body;
    const campusCode = novoCurso.id_campus.toString().padStart(2, '0');
    const cursoCode = `1${novoCurso.turno}10${campusCode}`;
    novoCurso.id = parseInt(cursoCode);
    db.cursos.push(novoCurso);
    res.send(`Curso ${novoCurso.nome} adicionado com sucesso!`);
});

// LER TUDO Cursos (GET)
router.get("/", (req, res) => {
    res.json(db.cursos);
});

// LER 1 Curso (GET)
router.get("/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const curso = db.cursos.find(curso => curso.id === cursoId);
    if (curso) {
        res.json(curso);
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

// ALTERAR Curso (PUT)
router.put("/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const updatedCurso = req.body;
    const index = db.cursos.findIndex(curso => curso.id === cursoId);
    if (index !== -1) {
        db.cursos[index] = updatedCurso;
        res.send(`Curso atualizado com sucesso!`);
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

// APAGAR Curso (DELETE)
router.delete("/:id", (req, res) => {
    const cursoId = parseInt(req.params.id);
    const index = db.cursos.findIndex(curso => curso.id === cursoId);
    if (index !== -1) {
        db.cursos.splice(index, 1);
        res.send("Curso removido com sucesso!");
    } else {
        res.status(404).send("Curso não encontrado.");
    }
});

module.exports = router;
