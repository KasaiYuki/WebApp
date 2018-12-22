import wolframalpha

def getResponse(uInput):
    app_id = "X496Y5-AAV2U7AJAR"
    client = wolframalpha.Client(app_id)

    res = client.query(uInput)
    answer = next(res.results).text
    return answer
