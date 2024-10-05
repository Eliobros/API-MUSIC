require('dotenv').config();  // Carrega as variáveis de ambiente do arquivo .env
const express = require('express');
const axios = require('axios');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search';
const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY; // Carrega a chave da API do arquivo .env

// Função para buscar vídeos no YouTube
const fetchVideos = async (query) => {
  try {
    const response = await axios.get(YOUTUBE_API_URL, {
      params: {
        q: query,
        part: 'snippet',
        maxResults: 10,
        key: YOUTUBE_API_KEY,
      }
    });
    return response.data.items;
  } catch (error) {
    throw new Error('Erro ao buscar vídeos do YouTube');
  }
};

// Rota para buscar filmes ou músicas
app.get('/search', async (req, res) => {
  const query = req.query.q; // Palavra-chave de busca
  if (!query) return res.status(400).send({ error: 'A query is required' });

  try {
    const results = await fetchVideos(query);
    res.send(results);  // Retorna a resposta ao cliente
  } catch (error) {
    res.status(500).send({ error: 'Error fetching videos' });
  }
});

// Implementação com socket.io (opcional)
io.on('connection', (socket) => {
  console.log('User connected');
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

// Inicia o servidor
const PORT = process.env.PORT || 3000;
http.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
