def test_edge_1(json_placeholder_edge):
    payload = {}
    res = json_placeholder_edge.post("/users",payload)
    print(res.status_code)
    assert res.status_code == 201
    max_55 = "x" * 255
    max_255 = "y" * 500
    payload2 = {
        "name": max_55,
        "email": max_55 + "@test.com",
        "address": max_255
    }
    res = json_placeholder_edge.post("/users",payload2)
    print(res.status_code)
    assert res.status_code == 201
    max_55 = "x" * 255
    max_255 = "y" * 500
    payload3 = {
        "name": "José María González-Pérez £$%^",
        "email": "josé@müller.com"
    }
    res = json_placeholder_edge.post("/users",payload3)
    print(res.status_code)
    assert res.status_code == 201