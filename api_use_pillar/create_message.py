import requests,json

# Get access token from a bot
ACCESS_TOKEN = "ZjI2MzBlNTQtMmYxNC00NTIyLWJmN2UtY2Q2MzY5ZmVjMDNiMTBlNDk1YjUtYzg1_PF84_955f323f-020d-4c86-9579-05f6f5cfbd1c"
# Get the roomID from https://developer.webex.com/docs/api/v1/rooms/list-rooms
roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNDMxNTMzNTAtODg4YS0xMWVjLWE0NTUtMTMyODFhYzhiYWVm"

m = {
    #"roomId": roomID,
    #"toPersonId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jZDgxOWIyZC01MzIyLTQ3NmItYmMxMS05MjBmOTVmZTBkYjk",
    "toPersonEmail": "diannazzo@lasegunda.com.ar",
    "text": "Tano esto es un test desde un bot de webex, soy matias"
}

r = requests.post(
    "https://webexapis.com/v1/messages",
    data=json.dumps(m),
    headers={
        "Authorization": "Bearer {}".format(ACCESS_TOKEN),
        "Content-Type": "application/json",
    },
)
print(r.status_code)


