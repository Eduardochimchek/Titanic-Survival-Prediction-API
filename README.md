# Titanic Survival Prediction API
## Descrição

Este repositório contém uma API RESTful simples construída com Flask para prever a sobrevivência de passageiros do Titanic. A API utiliza um modelo de aprendizado de máquina treinado com o dataset do Titanic para fazer previsões baseadas em informações como classe do passageiro, sexo, idade e outros atributos. A previsão é feita através de um endpoint que recebe dados em formato JSON e retorna a previsão de sobrevivência (1 para sobrevivente e 0 para não sobrevivente).

## Tecnologias Utilizadas

Flask - Framework web para construir a API.<br>
Scikit-learn - Biblioteca para treinamento e uso de modelos de aprendizado de máquina.<br>
Pandas - Biblioteca para manipulação de dados.<br>
Joblib - Biblioteca para salvar e carregar o modelo treinado.<br>
API REST - Para testar e interagir com a API via extensão no editor (como VSCode).<br>

## Pré-requisitos

## Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados:

Python 3.x<br>
pip (gerenciador de pacotes do Python)

## Instalação

### Clone o repositório:

git clone https://github.com/seu-usuario/Titanic-Survival-Prediction-API.git

### Navegue até o diretório do projeto:

cd Titanic-Survival-Prediction-API

### Crie e ative um ambiente virtual:

```
python -m venv venv<br>
```
source venv/bin/activate  # Para Linux/MacOS<br>
venv\Scripts\activate     # Para Windows<br>

### Instale as dependências do projeto:

pip install -r requirements.txt

Certifique-se de que o arquivo do modelo treinado (modelo_titanic.pkl) esteja na pasta model/.

## Como Usar

### Executando a API Localmente
### Inicie a aplicação Flask:

python app.py

A API estará disponível em http://127.0.0.1:5000/.

## Fazendo uma Requisição de Previsão

### Você pode testar a API utilizando a extensão API REST no seu editor ou qualquer ferramenta que suporte requisições HTTP como Postman.
### Crie uma requisição POST para o endpoint /predict com o seguinte corpo JSON:
```
{
    "Pclass": 3,
    "Sex": "female",
    "Age": 50,
    "SibSp": 1,
    "Parch": 1,
    "Fare": 30,
    "Embarked": "C"
}
```

### A resposta da API será no formato:
```
{
    "message": "Previsao realizada com sucesso!",
    "prediction": 1
}
```

### Onde:

"prediction" será 1 se o passageiro sobreviveu e 0 se não sobreviveu.

### Arquivo de Exemplo (api_titanic.http)
### Se você estiver usando a extensão API REST, use o seguinte conteúdo para testar a API diretamente:

```
POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
    "Pclass": 3,
    "Sex": "female",
    "Age": 50,
    "SibSp": 1,
    "Parch": 1,
    "Fare": 30,
    "Embarked": "C"
}
```

## Estrutura de Arquivos

Titanic-Survival-Prediction-API/<br>
── app.py                   * Código principal da API<br>
── model/                     * Pasta com o modelo treinado<br>
&nbsp;&nbsp;&nbsp;└── modelo_titanic.pkl     * Modelo de predição do Titanic<br>
── Titanic.csv               * Dataset do Titanic<br>
── Titanic_Machine_Learning.ipynb  * Jupyter Notebook de treinamento do modelo<br>
── api_titanic.http          * Arquivo para testar a API com a extensão API REST<br>
── requirements.txt          * Dependências do projeto<br>
── LICENSE                   * Licença do repositório<br>
── README.md                 * Este arquivo<br>

## Contribuições

Contribuições são bem-vindas! Para contribuir com o projeto, siga as etapas abaixo:

Faça um fork do repositório.<br>
Crie uma branch para a sua feature (git checkout -b feature/nome-da-feature).<br>
Faça as alterações desejadas e envie um commit (git commit -am 'Adiciona nova feature').<br>
Envie para o repositório original (git push origin feature/nome-da-feature).<br>
Abra um pull request.<br>

## Licença
Este projeto está licenciado pelo MIT
