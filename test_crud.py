import pytest_html
def test_crud_1(json_placeholder,go_resbase):
 import requests
 import time
 payload = {
  "title": "Test Post Title",
  "body": "This is a test post body content for automation testing",
  "userId": 2
 }
 headers = {
  "Authorization": "Bearer 1f40cdb0e901a1a5bff817d9acfbef1f3cb54b552e71fe24b85885c314fd0caf"
 }
 body = {
  "name": "John Doe Autzxczomation",
  "email": "aprazzsdzxcsdfsdfzxczcsafkas2@gmail.com",
  "gender": "male",
  "status": "active"
 }
 start = time.time()
 res = json_placeholder.post("/posts",payload,headers=headers)
 res_time = time.time()
 d = res_time - start
 print(res.status_code)
 a = res.json()
 print(a)
 assert a["id"] == 101
 li = ["title", "body", "userId", "id"]
 for r in li:
  assert r in a
 assert d < 1
 assert res.status_code == 201
 res_get = json_placeholder.get("/posts/1")
 print(res_get.status_code)
 print(res_get.json())
 a = res_get.json()
 assert "id" in a
 assert "title" in a
 assert "userId" in a
 assert "body" in a
 assert isinstance(a["id"], int)
 assert isinstance(a["userId"], int)
 assert isinstance(a["title"], str)
 assert isinstance(a["body"], str)
 res = go_resbase.post("/users",body,headers=headers)
 print("yes",res.status_code)
 a = res.json()
 print("yes",a)
 assert "id" in a
 #assert res.status_code==422,"error"
 li = ["id", "name", "email", "gender", "status"]
 for r in li:
  assert r in a

 #assert "taken" in a[0]["message"]