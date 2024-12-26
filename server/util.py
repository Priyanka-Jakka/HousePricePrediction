import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    with open("/Users/apple/Desktop/Projects/housepriceprediction/server/artifacts/columns.json",'r')as f:
        __data_columns=json.load(f)['data_columns']
        # print(__data_columns)
        __locations=__data_columns[3:]

    
    with open("/Users/apple/Desktop/Projects/housepriceprediction/server/artifacts/banglore_house_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)
    print("Loading of artifacts is done!!!")

def get_location_names():
    #print(__locations)
    return __locations


# if __name__=="__main__":
#     load_saved_artifacts()
#     # print(get_location_names())
#     print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
