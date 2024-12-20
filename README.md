# API para modelos de IA pré treinados

Este projeto tem como objetivo desenvolver uma API em python, utilizando o FastAPI, para que o usuário consiga interagir com os modelos pré treinados disponíveis no Ollama. 

## Funcionalidades
- Geração de respostas baseadas em prompts.
- Suporte à personalização de modelo e parâmetros de geração.
- Interface interativa gerada automaticamente pelo Swagger UI.

## Requisitos
- Python 3.9 ou superior
- FastAPI
- Uvicorn
- Cliente Ollama configurado localmente
- Host Ollama disponível (http://localhost:11434/)

### Instalação do Ollama

Para o host ollama ficar disponível em sua máquina, é necessário realizar a  instalação do [Ollama](https://github.com/ollama/ollama), acesse a documentação do ollama e siga o tutorial para instalar ele em sua máquina.

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
     pip install -r requirements.txt
    ```
4. Certifique-se de que o cliente Ollama está configurado e rodando no endereço http://localhost:11434/.

## Execução
1. No seu cmd, Inicie o servidor FastAPI:
    ```bash
    uvicorn main:app --reload
    ```
2. Acesse a interface interativa em:
    Swagger UI: http://127.0.0.1:8000/docs
    

## Endpoints
POST /generate-report
Gera um respostas baseado no prompt e nos parâmetros fornecidos.

Parâmetros
|Nome |	Tipo | Padrão | Descrição|
|-----|------|--------|----------|
|model|	string|Ex: "llama3.2:1b"|	Nome do modelo a ser utilizado
|prompt|string|Obrigatório|Texto do prompt para geração
|seed |	int|123|Seed para geração aleatória
|temperature |float|0.7|Controle de criatividade (0.0 a 1.0)
|min_tokens |int|200|Mínimo de tokens a serem gerados
|num_gpu |int|1|Número de GPUs a serem utilizadas
|main_gpu |int|0|ID da GPU principal

### Exemplo de Uso
 ```bash
     {
      "model": "llama3.2:1b",
      "prompt": "Explique o impacto da tecnologia na educação.",
      "seed": 42,
      "temperature": 0.8,
      "min_tokens": 150,
      "num_gpu": 1,
      "main_gpu": 0
    }
   ```
   
 ### Contribuição

1. Faça um fork do repositório.
2. Crie um branch para sua feature:

     ```bash
    uvicorn main:app --reload
    ```
3. Commit suas alterações:
     ```bash
    git commit -m "Descrição das mudanças"
    ```
4. Faça o push para o branch:
     ```bash
    git push origin feature/sua-feature
    ```
5. Abra um Pull Request.



