import pickle
from ml_service.drug.src.scripts.preparation import preprocessing
from ml_service.drug.src.scripts.modelling.tree import tree_model
from ml_service.drug.src.scripts.evaluation import evaluate
gender_map = {"F": 0, "M": 1}
bp_map = {"HIGH": 0, "LOW": 1, "NORMAL": 2}
cholestol_map = {"HIGH": 0, "NORMAL": 1}
drug_map = {0: "DrugY", 3: "drugC", 4: "drugX", 1: "drugA", 2: "drugB"}

def predict_drug(Age, 
                 Sex, 
                 BP, 
                 Cholesterol, 
                 Na_to_K):

    # 1. Read the machine learning model from its pickled state ...
    pickle_file = open('model.pkl', 'rb')     
    model = pickle.load(pickle_file)
    
    # 2. Transform the "raw" parameters passed into the function to the encoded numerical values using the maps dictionaries
    Sex = gender_map[Sex]
    BP = bp_map[BP]
    Cholesterol = cholestol_map[Cholesterol]

    # 3. Make an individual prediction for this set of data
    y_predict = model.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])[0]

    # 4. Return the "raw" version of the prediction i.e. the actual name of the drug rather than the numerical encoded version
    return drug_map[y_predict] 