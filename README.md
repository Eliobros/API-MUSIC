# Minha API de Busca de Filmes e Músicas

Esta API permite buscar filmes e músicas usando a YouTube API v3, retornando resultados baseados nas consultas feitas pelo usuário.

## Funcionalidades

- Buscar filmes ou músicas por meio de uma consulta (query) via YouTube API.
- Suporte a **Socket.io** para funcionalidades em tempo real.
- Configuração da API key via arquivo `.env` para maior segurança.

## Tecnologias Utilizadas

- **Node.js**: Ambiente de execução.
- **Express**: Framework para criação de servidores HTTP.
- **Axios**: Cliente HTTP para fazer requisições à API do YouTube.
- **Socket.io**: Para comunicação em tempo real (opcional).
- **Dotenv**: Para gerenciamento de variáveis de ambiente.

## Pré-requisitos

Você precisa ter instalado em sua máquina:

- [Node.js](https://nodejs.org/) v14 ou superior
- [NPM](https://www.npmjs.com/) (gerenciador de pacotes Node.js)
- Chave da API do YouTube [obtida aqui](https://console.developers.google.com/)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd seu-repositorio
   ```

3. Instale as dependências:

   ```bash
   npm install
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do YouTube:

   ```bash
   YOUTUBE_API_KEY=SUA_CHAVE_API_AQUI
   ```

## Uso

Para iniciar o servidor, execute o seguinte comando:

```bash
npm start
```

A API estará disponível em `http://localhost:3000`.

### Exemplo de Requisição

- **Buscar filmes ou músicas:**

  ```
  GET /search?q=musica
  ```

  - Parâmetro de consulta (`q`): O termo a ser buscado (ex: "música", "filmes de ação").
  - Retorna uma lista de vídeos do YouTube relacionados ao termo de busca.

## Funcionalidades Futuras

- Autenticação de usuários.
- Filtro avançado de resultados.
- Integração com outros serviços de música e filmes.

## Contribuição

Se desejar contribuir com este projeto, fique à vontade para abrir um **pull request** ou relatar problemas na seção de **issues**.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE)
