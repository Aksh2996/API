import pytest_html
def test_error_1(json_placeholder_error):
    import requests
    res_err = json_placeholder_error.get("/posts/99999")
    print(res_err.status_code)
    assert res_err.status_code == 404, "no error"
    a = res_err.json()
    print(a)
    assert a == {}
    res = json_placeholder_error.get("/invalid-endpoint")
    a = res.status_code
    b = res.json()
    c = res.text.lower()
    print(c)
    print(a)
    print(b)
    assert a == 404, "found"
    assert b == {}, "not empty"

def test_error_2(http_bin):
    res_del = http_bin.delete("/get")
    print(res_del.status_code)
    a = res_del.text
    print(a)
    assert res_del.status_code == 405, "false"
    assert "Method Not Allowed" in a, "fail"
    print(res_del.headers)
    print(type(res_del.headers))
    print(res_del.headers.get("Allow"))
    assert "GET" in res_del.headers.get("Allow")
    #assert "\get" in res_del.text, "in"