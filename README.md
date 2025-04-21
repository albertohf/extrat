# Análise de Solo - Extração de Texto em Imagens

## Descrição do Projeto

Este projeto implementa uma API para extração de texto de imagens de análises de solo usando técnicas de OCR (Reconhecimento Óptico de Caracteres). A aplicação utiliza o Tesseract OCR em conjunto com técnicas de pré-processamento de imagem para melhorar a qualidade da extração de texto.

## Funcionalidades

- Pré-processamento de imagens para melhorar o reconhecimento de texto
- Extração de texto via Tesseract OCR
- API RESTful para integração com outros sistemas
- Suporte a múltiplos idiomas (inglês e português por padrão)

## Requisitos

### Software necessário

- Python 3.11+
- Tesseract OCR 5.0+
- Docker (opcional, para deploy)

### Instalação do Tesseract OCR

#### Windows

1. Baixe o instalador do Tesseract OCR para Windows em: https://github.com/UB-Mannheim/tesseract/wiki
2. Execute o instalador e siga as instruções
3. O caminho padrão de instalação é `C:\Program Files\Tesseract-OCR\tesseract.exe`

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-por  # Para suporte ao português
```

## Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/soil-analysis.git
cd soil-analysis
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Verifique o caminho do Tesseract no arquivo `app/ocr_utils.py` e ajuste se necessário:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Executando a aplicação

### Localmente

Execute o seguinte comando para iniciar o servidor:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`

### Com Docker

Para executar com Docker:

```bash
docker build -t soil-analysis .
docker run -p 8000:8000 soil-analysis
```

### Com Docker Compose e Traefik (Ambiente Local)

1. Execute o script de configuração:

```bash
# Linux/Mac
bash setup.sh
# Windows (PowerShell)
./setup.sh
```

2. Inicie os serviços:

```bash
docker-compose up -d
```

3. Acesse a API em:
   - API: `http://localhost/`
   - Documentação: `http://localhost/docs`
   - Dashboard Traefik: `http://localhost/dashboard/`

## Utilizando a API

### Endpoints disponíveis

- `POST /extract_text/`: Extrair texto de uma imagem

### Documentação da API

- Swagger UI: `http://localhost/docs`
- ReDoc: `http://localhost/redoc`

### Exemplo de uso com curl

```bash
curl -X POST "http://localhost/extract_text/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@caminho/para/sua/imagem.jpg"
```

### Exemplo de resposta

```json
{
  "text": "Resultado da análise de solo:\nN: 10mg/kg\nP: 15mg/kg\nK: 25mg/kg\npH: 6.5"
}
```

## Estrutura do Projeto

```
soil-analysis/
├── app/
│   ├── __init__.py
│   ├── main.py            # Definição da API FastAPI
│   └── ocr_utils.py       # Funções de OCR e processamento de imagem
├── traefik/
│   └── traefik.yml        # Configuração do Traefik
├── Dockerfile             # Configuração para Docker
├── docker-compose.yml     # Configuração com Traefik
├── setup.sh               # Script de configuração
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

## Limitações Conhecidas

- O OCR pode ter dificuldades com fontes muito pequenas ou imagens de baixa qualidade
- Idiomas suportados padrão: inglês e português (configurável)

## Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.
