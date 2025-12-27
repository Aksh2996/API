def test_auths(req_res_helper):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "citysli"
    }
    headers = {
        "x-api-key": "reqres-free-v1",  # ← add this header
        "Content-Type": "application/json"  # good practice
    }
    r=req_res_helper.post("/login",payload,headers)
    print(r.status_code)