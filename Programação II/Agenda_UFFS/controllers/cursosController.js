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

// CRIAR Curso (POST)
router.post("/", async (req, res) => {
    try {
        const novoCurso = req.body;
        const campusCode = novoCurso.id_campus.toString().padStart(2, '0');
        const turno = novoCurso.turno;
        
        // Executar a consulta SQL para inserir o novo curso
        const query = `
            INSERT INTO curso (nome, turno, id_campus) 
            VALUES ($1, $2, $3)
            RETURNING id, nome`;
        const values = [novoCurso.nome, turno, novoCurso.id_campus];
        const result = await pool.query(query, values);

        // Retornar o ID e o nome do curso adicionado
        res.json({ id: result.rows[0].id, nome: result.rows[0].nome });
    } catch (error) {
        console.error('Erro ao adicionar curso:', error.message);
        res.status(500).send('Erro ao adicionar curso.');
    }
});

// LER TUDO Cursos (GET)
router.get("/", async (req, res) => {
    try {
        // Executar a consulta SQL para obter todos os cursos
        const result = await pool.query('SELECT * FROM curso');

        // Retornar os cursos encontrados
        res.json(result.rows);
    } catch (error) {
        console.error('Erro ao obter cursos:', error.message);
        res.status(500).send('Erro ao obter cursos.');
    }
});

// LER 1 Curso (GET)
router.get("/:id", async (req, res) => {
    try {
        const cursoId = parseInt(req.params.id);
        
        // Executar a consulta SQL para obter um curso específico
        const query = 'SELECT * FROM curso WHERE id = $1';
        const result = await pool.query(query, [cursoId]);

        // Verificar se o curso foi encontrado
        if (result.rows.length > 0) {
            res.json(result.rows[0]);
        } else {
            res.status(404).send("Curso não encontrado.");
        }
    } catch (error) {
        console.error('Erro ao obter curso:', error.message);
        res.status(500).send('Erro ao obter curso.');
    }
});

// ALTERAR Curso (PUT)
router.put("/:id", async (req, res) => {
    try {
        const cursoId = parseInt(req.params.id);
        const updatedCurso = req.body;
        
        // Executar a consulta SQL para atualizar o curso
        const query = `
            UPDATE curso 
            SET nome = $1, turno = $2, id_campus = $3 
            WHERE id = $4`;
        const values = [updatedCurso.nome, updatedCurso.turno, updatedCurso.id_campus, cursoId];
        await pool.query(query, values);

        res.send(`Curso ${cursoId} atualizado com sucesso!`);
    } catch (error) {
        console.error('Erro ao atualizar curso:', error.message);
        res.status(500).send('Erro ao atualizar curso.');
    }
});

// APAGAR Curso (DELETE)
router.delete("/:id", async (req, res) => {
    try {
        const cursoId = parseInt(req.params.id);
        
        // Executar a consulta SQL para excluir o curso
        const query = 'DELETE FROM curso WHERE id = $1';
        await pool.query(query, [cursoId]);

        res.send("Curso removido com sucesso!");
    } catch (error) {
        console.error('Erro ao excluir curso:', error.message);
        res.status(500).send('Erro ao excluir curso.');
    }
});

module.exports = router;
