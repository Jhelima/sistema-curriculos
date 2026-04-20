# Sistema de Cadastro de Candidatos - 
## 📝 Breve Descrição do Projeto
A aplicação foi construída focando em escalabilidade e isolamento de ambientes:
* **Frontend:** Interface desenvolvida em HTML5 semântico e CSS3, utilizando o servidor **Nginx** para alta performance.
* **Backend:** API REST desenvolvida em **Java com Spring Boot**, garantindo uma estrutura escalável e limpa.
* **Dados:** Utilizei **Python com a biblioteca Pandas** para o tratamento e limpeza prévia dos dados, otimizando a estrutura para o sistema.
* **Infraestrutura:** Deploy realizado no **Google Cloud Run**, com suporte a HTTPS e escalabilidade automática.

## 📂 Estrutura do Código Fonte
O repositório está organizado da seguinte forma:
* `/frontend`: Interface do usuário e configuração do servidor Nginx.
* `/backend`: Código fonte da API Java Spring Boot.
* `/data`: Scripts Python para manipulação de dados e arquivos CSV/SQL.
* `docker-compose.yml`: Orquestração de todos os containers da aplicação local.

### 1. Execução Local (Docker)
Para rodar o projeto completo localmente, é necessário ter o Docker instalado:
1. No terminal, acesse a pasta raiz do projeto.
2. Execute o comando:
   ```bash
   docker-compose up --build
