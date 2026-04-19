FROM nginx:alpine

# Remove arquivos padrão
RUN rm -rf /usr/share/nginx/html/*

# Copia arquivos (index.html, recrutador.html, index.css)
COPY . /usr/share/nginx/html

# Cria um arquivo de configuração NOVO e SIMPLES direto na porta 8080
RUN echo 'server { \
    listen 8080; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
