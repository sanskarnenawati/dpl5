import joblib


def predict(data):
    lr = joblib.load('rentpred.sav')
    return lr.predict(data)
    rt = joblib.load('label_encoder.sav')
    return lr.predict(data)
 t = pockle.load('scaler.pkl')
    return lr.predict(data)
