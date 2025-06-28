const express = require('express');
const { Pool } = require('pg');
const router = express.Router();

// Configuração do banco de dados
const pool = new Pool({
    user: 'jonathan',
    password: '159789',
    host: 'localhost',
    port: 5432,
    database: 'prog2'
});

// CRIAR CCR (POST)
router.post("/", async (req, res) => {
    try {
        const novoCCR = req.body;
        const query = 'INSERT INTO ccr (id, nome) VALUES ($1, $2) RETURNING *';
        const values = [novoCCR.id, novoCCR.nome];
        const result = await pool.query(query, values);
        res.json(result.rows[0]);
    } catch (error) {
        console.error('Erro ao criar CCR:', error.message);
        res.status(500).send('Erro ao criar CCR.');
    }
});

// LER TUDO CCRs (GET)
router.get("/", async (req, res) => {
    try {
        const query = 'SELECT * FROM ccr';
        const result = await pool.query(query);
        res.json(result.rows);
    } catch (error) {
        console.error('Erro ao obter CCRs:', error.message);
        res.status(500).send('Erro ao obter CCRs.');
    }
});

// LER 1 CCR (GET)
router.get("/:id", async (req, res) => {
    try {
        const ccrId = req.params.id;
        const query = 'SELECT * FROM ccr WHERE id = $1';
        const result = await pool.query(query, [ccrId]);

        if (result.rows.length > 0) {
            res.json(result.rows[0]);
        } else {
            res.status(404).send("CCR não encontrado.");
        }
    } catch (error) {
        console.error('Erro ao obter CCR:', error.message);
        res.status(500).send('Erro ao obter CCR.');
    }
});

// ALTERAR CCR (PUT)
router.put("/:id", async (req, res) => {
    try {
        const ccrId = req.params.id;
        const updatedCCR = req.body;
        const query = 'UPDATE ccr SET nome = $1 WHERE id = $2';
        const values = [updatedCCR.nome, ccrId];
        await pool.query(query, values);
        res.send("CCR atualizado com sucesso!");
    } catch (error) {
        console.error('Erro ao atualizar CCR:', error.message);
        res.status(500).send('Erro ao atualizar CCR.');
    }
});

// APAGAR CCR (DELETE)
router.delete("/:id", async (req, res) => {
    try {
        const ccrId = req.params.id;
        const query = 'DELETE FROM ccr WHERE id = $1';
        await pool.query(query, [ccrId]);
        res.send("CCR removido com sucesso!");
    } catch (error) {
        console.error('Erro ao excluir CCR:', error.message);
        res.status(500).send('Erro ao excluir CCR.');
    }
});

module.exports = router;
