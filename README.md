# 📦 Inventory Control System (Controle de Estoque)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%23499848.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

Um sistema web completo de **Controle de Estoque** desenvolvido em Python com o framework Django. O projeto foi projetado para facilitar o gerenciamento de produtos, o acompanhamento de quantidades e o registro do histórico de movimentações (entradas e saídas).

## 🎯 Objetivos do Projeto

O objetivo principal deste projeto é fornecer uma ferramenta intuitiva e eficiente para a gestão de inventário. Funcionalidades de destaque incluem:
- **Cadastro de Produtos:** Adição de novos itens detalhando código, nome, categoria e exigência mínima de estoque.
- **Acompanhamento de Saldos:** Visão clara e em tempo real da quantidade atual de todos os produtos do estoque.
- **Registro de Movimentações:** Ferramenta dedicada para lançamento de entradas e saídas de um produto específico, mantendo um histórico auditável das operações.
- **Prevenção de Rupturas:** Emissão de alertas visuais e automáticos (⚠ **ESTOQUE BAIXO**) sempre que um produto atinge ou fica abaixo do seu limite seguro.

## 🚀 Tecnologias e Frameworks

Este projeto foi construído utilizando as seguintes tecnologias:
- **[Python](https://www.python.org/)** - Linguagem back-end ágil e poderosa.
- **[Django](https://www.djangoproject.com/)** - Framework web robusto que incentiva o desenvolvimento limpo, seguro e rápido.
- **HTML5 & CSS3** - Estruturação e estilização das páginas, proporcionando uma interface limpa e elegante.
- **SQLite3** - Banco de dados embutido utilizado para armazenar os registros do estoque (padrão do Django).

## 🛠️ Como Executar o Projeto Localmente

Siga o passo a passo abaixo para rodar o sistema no seu seu ambiente local:

1. **Clone este repositório**
   ```bash
   git clone https://github.com/DerickxP/inventory-control-system.git
   cd inventory-control-system
   ```

2. **Crie e ative um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # No Windows
   venv\Scripts\activate
   
   # No Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências requeridas**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```
   Acesse a aplicação no seu navegador padrão pelo endereço: `http://localhost:8000/`.

## 📂 Estrutura do Projeto

- `controle/`: App principal contendo a lógica de negócios, Models (tabelas do banco de dados), Views, e rotas locais.
- `estoque/`: Ponto de entrada e diretório de configurações principais do projeto Django.
- `templates/`: Páginas HTML.
- `static/`: Recursos estáticos incluindo folhas de estilo em CSS.

---

💼 Projeto desenvolvido por [DerickxP](https://github.com/DerickxP)
