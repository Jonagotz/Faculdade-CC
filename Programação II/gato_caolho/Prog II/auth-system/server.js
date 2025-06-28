const express = require('express');
//é um middleware que analisa os corpos das requisições HTTP, tornando os dados acessíveis em req.body.
const bodyParser = require('body-parser');
const session = require('express-session');
//é um middleware para autenticação em Node.js, suportando diversos métodos de autenticação.
const passport = require('passport');
//é uma estratégia de autenticação do passport que usa nome de usuário e senha
const LocalStrategy = require('passport-local').Strategy;
// criptografia
const bcrypt = require('bcryptjs');
//Veirificaçao e autenticidade de token json;
const jwt = require('jsonwebtoken');
// Requisições de mais de uma origem
const cors = require('cors');

// Inicializa o servidor na porta 5000
const app = express();
const PORT = 5000; 

// Configuração do body-parser
app.use(bodyParser.urlencoded({ extended: false })); // para uso no formulario html
app.use(bodyParser.json()); // para uso de API

// Configuração do CORS
app.use(cors());

// Configuração da sessão
app.use(session({
  // Define uma string secreta usada para assinar e verificar o cookie da sessão.
  secret: 'secret',
  // Se `false`, a sessão não será salva de volta ao armazenamento de sessão se não for modificada 
  // durante a requisição.
  resave: false,
  // Se `true`, uma nova sessão, mesmo não modificada, será salva no armazenamento de sessão.
  saveUninitialized: true
}));


// Inicialização do Passport
app.use(passport.initialize()); // Precisa ser inicializado para ser utilizado
app.use(passport.session()); // Esta linha integra o Passport com o middleware de sessão do Express.
// Habilita o suporte à sessão para que o Passport possa persistir a autenticação do usuário entre diferentes requisições HTTP.

// Usuário fixo para teste com senha hash bcrypt
const user = {
  id: 1,
  username: 'user',
  password: bcrypt.hashSync('password', 10) // Armazena a senha criptografada
};

// Configuração do Passport Local Strategy
passport.use(new LocalStrategy((username, password, done) => {
  if (username === user.username) {
    bcrypt.compare(password, user.password, (err, isMatch) => {
      if (err) throw err;
      if (isMatch) {
        return done(null, user);
      } else {
        return done(null, false, { message: 'Senha incorreta' });
      }
    });
  } else {
    return done(null, false, { message: 'Usuário não encontrado' });
  }
}));

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  if (id === user.id) {
    done(null, user);
  } else {
    done({ message: 'Usuário não encontrado' }, null);
  }
});

// Rota de login
app.post('/login', (req, res, next) => {
  passport.authenticate('local', (err, user, info) => {
    if (err) throw err;
    if (!user) res.status(401).send(info.message);
    else {
      req.logIn(user, (err) => {
        if (err) throw err;
        const token = jwt.sign({ id: user.id }, 'jwt_secret_key', { expiresIn: '1h' });
        res.json({ token });
      });
    }
  })(req, res, next);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
