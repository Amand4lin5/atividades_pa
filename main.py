from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, Field
from ollama import Client

# Define the app
app = FastAPI()

# Initialize the client
client = Client(host='http://localhost:11434/')

@app.post("/generate-report")
async def generate_report(
    model: str = Form(default="llava:latest", description="Nome do modelo a ser utilizado"),
    prompt: str = Form(..., description="Texto do prompt para geração"),
    seed: int = Form(default=123, description="Seed para geração aleatória"),
    temperature: float = Form(default=0.7, ge=0.0, le=1.0, description="Controle de criatividade (0.0 a 1.0)"),
    min_tokens: int = Form(default=200, ge=1, description="Mínimo de tokens a serem gerados"),
    num_gpu: int = Form(default=1, ge=1, description="Número de GPUs a serem utilizadas"),
    main_gpu: int = Form(default=0, ge=0, description="ID da GPU principal"),
):
    try:
        # Extract the parameters
        options = {
            "seed": seed,
            "temperature": temperature,
            "min_tokens": min_tokens,
            "num_gpu": num_gpu,
            "main_gpu": main_gpu
        }

        # Generate response using Ollama
        response = client.generate(
            model=model,
            prompt=prompt,
            stream=False,
            options=options
        )

        # Return the response as JSON
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app with Uvicorn if needed
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
