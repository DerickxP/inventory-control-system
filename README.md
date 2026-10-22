# Controle de estoque em Django

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

Aplicação web para controlar o estoque de produtos: cadastro, saldo atual de cada
item, lançamento de entradas e saídas e alerta quando um produto fica abaixo do
estoque mínimo.

## Funcionalidades

- **Cadastro de produtos** com código (único), nome, categoria e estoque mínimo.
- **Lista de produtos** ordenada por nome, com o saldo atual e o estoque mínimo de cada um.
- **Alerta de estoque baixo** (`⚠ ESTOQUE BAIXO`) quando o saldo fica abaixo do mínimo.
- **Movimentações de entrada e saída** com quantidade e observação. Cada lançamento é
  gravado com data e hora e atualiza o saldo do produto.
- **Validações:** a quantidade precisa ser maior que zero e uma saída não pode ser
  maior que o saldo atual.
- **Admin do Django** com busca e filtros para produtos e para o histórico de movimentações.

## Como funciona

| Rota | O que faz |
|---|---|
| `/` | Lista de produtos com saldo e alerta |
| `/produtos/novo/` | Cadastro de produto |
| `/produtos/<id>/movimentacao/` | Lançamento de entrada ou saída |
| `/admin/` | Administração de produtos e movimentações |

O modelo tem duas tabelas: `Produto` e `Movimentacao`, ligada ao produto. O saldo
fica em `Produto.quantidade_atual` e é atualizado a cada movimentação.

```
controle/   # app: models, views, rotas, templates e CSS
estoque/    # configurações do projeto Django
```

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # opcional, para acessar /admin/
python manage.py runserver
```

Acesse `http://localhost:8000/`. O banco é um SQLite criado na primeira migração.

## Limitações

- As telas de produtos e movimentações não exigem login; só o `/admin/` é protegido.
- O histórico de movimentações só pode ser consultado pelo admin.
- O modelo tem preço de compra e de venda, mas o formulário de cadastro ainda não preenche esses campos.
- O projeto está configurado para desenvolvimento (`DEBUG = True`) e ainda não tem testes automatizados.

## Licença

[MIT](LICENSE)
