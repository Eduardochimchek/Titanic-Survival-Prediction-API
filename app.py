# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Inicializar o Flask
app = Flask(__name__)

# Carregar o modelo treinado
model = joblib.load('model/melhor_modelo_titanic.pkl')

# Definir o mapeamento para 'Sex' e 'Embarked'
sex_mapping = {"male": 0, "female": 1}
embarked_mapping = {"C": 0, "Q": 1, "S": 2}

# Carregar o scaler utilizado para a padroniza��o (assumindo que foi salvo em 'scaler.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Obter os dados da requisi��o
    data = request.get_json()

    # Mapear 'Sex' e 'Embarked' para valores num�ricos
    data['Sex'] = sex_mapping.get(data['Sex'], -1)  # Valor -1 se n�o encontrar
    data['Embarked'] = embarked_mapping.get(data['Embarked'], -1)  # Valor -1 se n�o encontrar

    # Preparar os dados de entrada para o modelo
    input_data = np.array([[data["Pclass"], data["Sex"], data["Age"], data["SibSp"], data["Parch"], data["Fare"], data["Embarked"]]])

    # Escalar os dados
    data_scaled = scaler.transform(input_data)

    # Realizar a predi��o
    prediction = model.predict(data_scaled)

    # Retornar a predi��o como resposta JSON
    return jsonify({"prediction": int(prediction[0]), "message": "Previsao realizada com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)