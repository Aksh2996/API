import datetime
import requests
import time
import pytest
import pytest_html
base_url="https://JSONplaceholder.typicode.com/posts"

def test_1(json_placeholder_perf):
    start=time.time()
    res=json_placeholder_perf.get("/posts")
    end=time.time()
    ms=(end-start)*1000
    print(f"{ms:.2f}")
    assert res.status_code==200
    assert ms<1000
def test_2(json_placeholder_perf):
    start=time.time()
    res=json_placeholder_perf.get("/posts")
    end=time.time()
    ms=(end-start)*1000
    print(f"{ms:.2f}")
    print(res.json())
    assert res.status_code==200
    assert ms<500
def test_3(json_placeholder_perf):
    start=time.time()
    payload={"title": "Performance API Test",
        "body": "Validating POST response time",
        "userId": 10
             }
    res=json_placeholder_perf.post2("/posts",payload)
    end=time.time()
    ms=(end-start)*1000
    assert res.status_code==201
    assert ms < 1000
    print(f"{ms:.2f}")
def test_perf_2(http_bin):
    import requests
    import time
    from concurrent.futures import ThreadPoolExecutor
    total_req = 10
    def re(i):
        start = time.time()
        res = http_bin.get("/delay/1")
        end = time.time()
        return {
            "req no": i,
            "status": res.status_code,
            "res_time": round((end - start) * 1000, 2)
        }

    if __name__ == "__main__":
        start1 = time.time()
        with ThreadPoolExecutor(max_workers=10) as e:
            results = e.map(re, range(1, total_req + 1))
        end1 = time.time()

        for res in results:
            print(res)
        total_req1 = round((end1 - start1) * 1000, 1)
        print(total_req1)
def test_perf_4(http_bin):
    import requests
    import json
    import time
    base_url = "https://httpbin.org/post"
    payload = {
        "data": "x" * 1024
    }
    tot_req = 50
    responses = []
    errors = 0
    start_test = time.time()
    for i in range(tot_req):
        req_start = time.time()
        try:
            res = http_bin.post("/post")
            req_end = time.time()
            times = (req_end - req_start) * 1000
            responses.append(times)

            if res.status_code != 200:
                errors = errors + 1
        except Exception:
            errors = errors + 1

        time.sleep(30 / tot_req)
    end_time = time.time()
    to = end_time - start_test
    success_rate = ((tot_req - errors) / tot_req) * 100
    ave = sum(responses) / len(responses)

    print("totaltime:", to)
    print("totalrequests", tot_req)
    print("errors", errors)
    print("success_rate", success_rate)
    print("avg_res_time", ave)
    assert success_rate > 95
    assert ave < 1500


