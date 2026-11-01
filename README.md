# API Biblioteca

API REST para controle de livros de uma biblioteca, feita com FastAPI e Pydantic. Os dados ficam em memória, então são perdidos quando o servidor reinicia.

**Aluno:** Lucas Bezerra

## Como rodar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
fastapi dev main.py
```

Documentação (Swagger): http://127.0.0.1:8000/docs

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/livros` | Lista livros (filtros opcionais: `autor`, `disponivel`) |
| GET | `/livros/{id}` | Busca um livro |
| POST | `/livros` | Cadastra um livro |
| PUT | `/livros/{id}` | Atualiza um livro |
| DELETE | `/livros/{id}` | Remove um livro |

Exemplo de corpo para POST/PUT:

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899,
  "disponivel": true
}
```
