const express = require('express');
const db = require('../models/database');
const router = express.Router();

// CRIAR CCR (POST)
router.post("/", (req, res) => {
    const novoCCR = req.body;
    db.ccrs.push(novoCCR);
    res.send("CCR adicionado com sucesso!");
});

// LER TUDO CCRs (GET)
router.get("/", (req, res) => {
    res.json(db.ccrs);
});

// LER 1 CCR (GET)
router.get("/:id", (req, res) => {
    const ccrId = req.params.id;
    const ccr = db.ccrs.find(ccr => ccr.id === ccrId);
    if (ccr) {
        res.json(ccr);
    } else {
        res.status(404).send("CCR não encontrado.");
    }
});

// ALTERAR CCR (PUT)
router.put("/:id", (req, res) => {
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
router.delete("/:id", (req, res) => {
    const ccrId = req.params.id;
    const index = db.ccrs.findIndex(ccr => ccr.id === ccrId);
    if (index !== -1) {
        db.ccrs.splice(index, 1);
        res.send("CCR removido com sucesso!");
    } else {
        res.status(404).send("CCR não encontrado.");
    }
});

module.exports = router;
