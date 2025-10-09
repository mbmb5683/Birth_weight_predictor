from app import app

#first positive test case for "/hello" route
# def test_hello_route_success ():
#       tester=app.test_client()
#       response = tester.get("/hello")


#       assert response.status_code==200


#negative test case for "/hello" route
# def test_hello_route_success ():
#       tester=app.test_client()
#       response = tester.get("/hello")


#       assert response.status_code==500


#first postive test case for "/predict" route
# data= {
#         "gestation": [280],
#         "parity":[0],
#         "age":[28],
#         "height":[170],
#         "weight":[70],
#         "smoke": [0]
# }

# def test_predict_route_success ():
#       tester=app.test_client()
#       response = tester.post("/predict", json= data)
#       assert response.status_code==200





#negative test case for "/predict" route

data= {
        "gestation": ["280"],
        "parity":[0],
        "age":[28],
        "height":[170],
        "weight":[70],
        "smoke": [0]
}

def test_predict_route_invalid_data ():
      tester=app.test_client()
      response = tester.post("/predict", json= data)
      assert response.status_code==400




#negative test case for "/predict" route

data= {
        "gestation": [280],
        "parity":[0],
        "age":[28],
        "height":[170],
        "weight":[70],
        "smoke": [0]
}

def test_predict_route_wrong_url ():
      tester=app.test_client()
      response = tester.post("/oredict", json= data)
      assert response.status_code==404




#negative test case for "/predict" route


data= {
        "gestation": [280],
        "parity":[0],
        "age":[28],
        "height":[170],
        "weight":[70],
        "smoke": [0]
}

def test_predict_route_wrong_method ():
      tester=app.test_client()
      response = tester.get("/predict", json= data)
      assert response.status_code==405