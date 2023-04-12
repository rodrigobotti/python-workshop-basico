# Workshop básico de python

## Introdução

Esse repositório contém conteúdo de um workshop básico de python ministrado para uma turma de pessoas que seguiram curso introdutório com os assuntos:
- introdução a programação com Java
- introdução a programação com Javascript
- bancos de dados relacionais
- aplicações web com Java usando SpringBoot

## Conteúdo

### Workshop

Durante o workshop foram criados os seguintes arquivos:
- [pyproject.toml](./pyproject.toml): manifesto de configuração do projeto usando [poetry](https://python-poetry.org/) como gerenciador de pacotes
- [main.py](./main.py): código que escrevemos durante o workshop — servidor de API REST de gestão de tarefas feitas utilizando o [Flask](https://flask.palletsprojects.com/en/2.2.x/) e o [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

### Extras

Alguns assuntos fundamentais de python foram pincelados rapidamente de forma não muito aprofundada durante o workshop.

- [basics.py](./basics.py):
    - classes e objetos
    - decorators
    - comprehensions

## Executar

Para poder executar todos os arquivos desse projeto é necessário preparar o ambiente de desenvolvimento.

Esse ambiente vai necessitar das seguintes dependências instaladas:
- [python 3.10](https://www.python.org/downloads/release/python-3100/) ou maior
- [poetry](https://python-poetry.org/)

### Utilizando o repl.it

Para facilitar esse processo -- caso você já não tenha essas dependências instaladas localmente em alguma máquina que você tem acesso -- é mais fácil criar um ambiente online com o `repl.it` ao invés de tentar montá-lo do zero.

Para isso, basta
- acessar o [repl.it](https://replit.com/)
- criar um novo repl
- utilizar o template `Python` do próprio `repl.it` -- já vem com o poetry instalado e configurado