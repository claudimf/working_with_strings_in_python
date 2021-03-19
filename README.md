# Trabalhando com strings com Python

👋 Olá, Seja Bem-vindo(a) ao 'trabalhando com strings com Python'.

# Projeto 'Trabalhando com strings com Python' do curso:

## [Python: Manipulação de Strings](https://cursos.alura.com.br/course/python-manipulando-strings)

### Aulas

<details>
    <summary>Fatiando string</summary>
    <ul>
        <li>Introdução</li>
        <li>Iniciando com Strings</li>
        <li>Fatiamento e índices de strings</li>
        <li>O método find</li>
        <li>Fatiamento de Strings</li>
        <li>Para saber mais</li>
        <li>Usando o método find()</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Soluções aplicando métodos de strings</summary>
    <ul>
        <li>None, empty e o if do Python</li>
        <li>Como o if funciona</li>
        <li>Construindo mais métodos</li>
        <li>O método Len</li>
        <li>Explorando as Strings</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Mais sobre métodos de strings</summary>
    <ul>
        <li>O método replace</li>
        <li>Upper e Lower</li>
        <li>Validação do site</li>
        <li>Explorando métodos string</li>
        <li>Começa com o que queremos?</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Expressões Regulares</summary>
    <ul>
        <li>O que são expressões regulares</li>
        <li>Regex com quantificadores</li>
        <li>Quantificadores com Intervalos</li>
        <li>Testando regex</li>
        <li>Mãos na massa</li>
        <li>Mais sobre Regex</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Métodos Especiais</summary>
    <ul>
        <li>Métodos especiais</li>
        <li>Dando um nome a nossa classe</li>
        <li>Comparando instâncias</li>
        <li>Conclusão</li>
        <li>Representação string</li>
        <li>Para saber mais</li>
        <li>Métodos especiais Python</li>
        <li>O método __eq__()</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>


# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Regular expression operations](https://docs.python.org/3/library/re.html)