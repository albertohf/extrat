#!/bin/bash

# Criar estrutura de diretórios
mkdir -p traefik/dynamic
mkdir -p traefik/logs

# Criar e ajustar permissões do arquivo acme.json para certificados
touch traefik/acme.json
chmod 600 traefik/acme.json

# Criar redes Docker se não existirem
if ! docker network ls | grep -q traefik-network; then
    echo "Criando rede traefik-network..."
    docker network create traefik-network
fi

if ! docker network ls | grep -q internal-network; then
    echo "Criando rede internal-network..."
    docker network create internal-network
fi

echo "Configuração concluída! Execute 'docker-compose up -d' para iniciar os serviços." 