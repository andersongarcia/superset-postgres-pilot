# Superset + PostgreSQL Pilot Starter Kit

Este repositório fornece uma infraestrutura agnóstica e pronta para uso do **Apache Superset** conectado a um banco de dados **PostgreSQL** via Docker. Ideal para exploração de funcionalidades, prototipagem de dashboards e testes de performance.

## 🛠️ Pré-requisitos

* **Docker** e **Docker Compose** instalados.
* **Python 3.x** na máquina local (necessário para rodar o script de população de dados).

---

## 🏁 Como Iniciar o Ambiente

### 1. Construir e Subir os Containers

Abra o terminal na pasta raiz do projeto e execute:

```bash
docker-compose up -d --build
```

### 2. Acessar o Superset

Execute os comandos abaixo em sequência para configurar o usuário administrador, o banco de metadados interno e as permissões:

```bash
# 1. Criar usuário administrador (Login: admin / Senha: admin)
docker exec -it superset_app superset fab create-admin --username admin --firstname Admin --lastname User --email admin@fab.org --password admin

# 2. Executar migrações do banco de dados interno
docker exec -it superset_app superset db upgrade

# 3. Inicializar componentes e visualizações padrão
docker exec -it superset_app superset init
```

### 4. Instalar Dependências e Popular o Banco

Para testar o ambiente com dados reais, instale os pacotes Python necessários e execute o script de geração de dados:

```bash
# Instalação das bibliotecas necessárias
pip install -r requirements.txt

# Execução do script de população
python gerar_dados.py
```

## 🔗 Conexão com o Banco no Superset

1. Acesse o painel do Superset em: `http://localhost:8088` (Credenciais: `admin` / `admin`).
2. No menu superior direito, vá em **Settings** (ícone de engrenagem) > **Database Connections**.
3. Clique no botão azul **+ Database**.
4. Selecione **PostgreSQL** na lista de bancos suportados.
5. No campo **SQLAlchemy URI**, utilize a string de conexão abaixo:

    ```text
    postgresql://superset_user:superset_password@db:5432/pilot_db
    ```

    * **Importante:** Note o uso do nome `db`. Como o Superset está rodando dentro de um container, ele utiliza o nome do serviço definido no `docker-compose` para localizar o banco de dados na rede interna do Docker.

6. Clique em **Test Connection**. Ao receber a mensagem de sucesso, clique em **Connect** ou **Finish**.

## 📂 Estrutura de Arquivos

* `Dockerfile`: Configuração para customizar a imagem oficial do Apache Superset, garantindo a instalação dos drivers do PostgreSQL (`psycopg2-binary`).
* `docker-compose.yml`: Orquestração dos serviços, definindo as redes internas, volumes para persistência de dados e as variáveis de ambiente (como a `SUPERSET_SECRET_KEY`).
* `requirements.txt`: Lista de dependências Python necessárias para executar o script de população de dados localmente.
* `gerar_dados.py`: Script de automação que utiliza a biblioteca Faker para gerar 300 registros aleatórios e inseri-los no banco de dados para testes imediatos.
* `README.md`: Documentação técnica com o passo a passo para instalação, configuração e uso do ambiente.
