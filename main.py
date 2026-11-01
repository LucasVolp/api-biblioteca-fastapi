from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API Biblioteca")


class LivroIn(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    autor: str = Field(min_length=1, max_length=120)
    ano: int = Field(ge=0, le=2100)
    disponivel: bool = True


class LivroOut(LivroIn):
    id: int


livros: dict[int, LivroOut] = {}
proximo_id = 1


def buscar_livro(livro_id: int) -> LivroOut:
    if livro_id not in livros:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Livro não encontrado")
    return livros[livro_id]


@app.get("/livros", response_model=list[LivroOut])
def listar_livros(autor: str | None = None, disponivel: bool | None = None):
    resultado = list(livros.values())
    if autor:
        resultado = [l for l in resultado if autor.lower() in l.autor.lower()]
    if disponivel is not None:
        resultado = [l for l in resultado if l.disponivel == disponivel]
    return resultado


@app.get("/livros/{livro_id}", response_model=LivroOut)
def obter_livro(livro_id: int):
    return buscar_livro(livro_id)


@app.post("/livros", response_model=LivroOut, status_code=status.HTTP_201_CREATED)
def criar_livro(dados: LivroIn):
    global proximo_id
    livro = LivroOut(id=proximo_id, **dados.model_dump())
    livros[proximo_id] = livro
    proximo_id += 1
    return livro


@app.put("/livros/{livro_id}", response_model=LivroOut)
def atualizar_livro(livro_id: int, dados: LivroIn):
    buscar_livro(livro_id)
    livros[livro_id] = LivroOut(id=livro_id, **dados.model_dump())
    return livros[livro_id]


@app.delete("/livros/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_livro(livro_id: int):
    buscar_livro(livro_id)
    del livros[livro_id]
