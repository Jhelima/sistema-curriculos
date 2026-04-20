A aplicação foi construída focando em escalabilidade e isolamento de ambientes:

Frontend: Interface desenvolvida em HTML5 semântico e CSS3, utilizando o servidor Nginx para alta performance.

Backend: API REST desenvolvida em Java com Spring Boot, garantindo uma estrutura escalável e limpa.

Dados: Utilizei Python com a biblioteca Pandas para o tratamento e limpeza prévia dos dados, otimizando a estrutura para o sistema antes da persistência.

Infraestrutura: Deploy realizado no Google Cloud Run, com suporte a HTTPS e escalabilidade automática.

📂 Estrutura do Código Fonte
O repositório está organizado da seguinte forma:

/frontend: Interface do usuário (HTML, CSS, JS) e configuração do servidor Nginx.

/backend: Código fonte da API Java Spring Boot.

/data: Scripts Python para manipulação de dados e arquivos CSV.

docker-compose.yml: Orquestração de todos os containers da aplicação para ambiente local.

🚀 Instruções de Execução
1. Execução Local (Docker)
Para rodar o projeto completo localmente, é necessário ter o Docker instalado:

No terminal, acesse a pasta raiz do projeto (sistema-curriculos).

Execute o comando:

Bash
docker-compose up --build
Acesse no navegador:

Frontend: http://localhost

API Backend: http://localhost:8080/candidatos

2. Acesso em Produção (Nuvem)
O projeto está disponível online nos endereços abaixo:

Interface do Candidato: https://frontend-sistema-1010907062664.us-central1.run.app

Painel do Recrutador: https://frontend-sistema-1010907062664.us-central1.run.app/recrutador.html

Endpoint da API (JSON): https://backend-java-1010907062664.us-central1.run.app/candidatos

🛠️ Tecnologias Utilizadas
Java 17 / Spring Boot

Python 3 / Pandas

Nginx

Docker & Docker Compose

Google Cloud Platform (Cloud Run)

Desenvolvido por: Jéssica Lima