import pytest
def test_valid_1(go_resbase):
    import requests
    head = {
        "Authorization": "Bearer 1f40cdb0e901a1a5bff817d9acfbef1f3cb54b552e71fe24b85885c314fd0caf"
    }
    body = {
        "name": "John Dxcvoe"
    }
    val_res =go_resbase.post("/users",body,head)
    print(val_res.status_code)
    assert val_res.status_code == 422
    print(val_res.text)
    d = val_res.json()
    assert isinstance(d, list)
    a = []
    for i in d:
        a.append(i["field"])
    print(a)
    b = ['email', 'gender', 'status']
    for field in b:
        assert field in a

def test_valid_3(go_resbase):
    import requests
    head = {
        "Authorization": "Bearer 1f40cdb0e901a1a5bff817d9acfbef1f3cb54b552e71fe24b85885c314fd0caf"
    }
    body = {
        "name": "John Dxcvoe",
        "email": "john@exsdfsample.com",
        "gender": "unknown",
        "status": "maybe"
    }
    res_vals = go_resbase.post("/users",body,head)
    print(res_vals.status_code)
    print(res_vals.json())

    a = res_vals.json()
    for i in a:
        if i["field"] == "gender":
            print(f"{i['field']}:", i["message"])
            assert "blank" in i["message"] or "invalid" in i["message"], "fail"
        if i["field"] == "status":
            print(f"{i['field']}:", i["message"])
            assert "blank" in i["message"] or "invalid" in i["message"], "fail"

def test_valid_2(go_resbase):
    import requests
    head = {
        "Authorization": "Bearer 1f40cdb0e901a1a5bff817d9acfbef1f3cb54b552e71fe24b85885c314fd0caf"
    }
    body = {
        "name": "John Doxcve",
        "email": "invalid-email-format",
        "gender": "male",
        "status": "active"
    }
    val_res = go_resbase.post("/users",body,head)
    print(val_res.status_code)
    assert val_res.status_code == 422
    print(val_res.text)
    d = val_res.json()
    print(val_res.text)
    assert "email" in d[0]["field"]
    assert "invalid" in d[0]["message"]
    print(len(d))