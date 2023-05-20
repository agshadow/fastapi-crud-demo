
working scripts:
1:

Invoke-WebRequest -Method 'Post' -Uri http://127.0.0.1:8000/tracks/ -Body '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}' -ContentType "application/json"

2:
$Url = 'http://127.0.0.1:8000/tracks/'
$Form = '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}'
Invoke-WebRequest -Method 'Post' -Uri $Url -Body $Form -ContentType "application/json"


3:
$Url = 'http://127.0.0.1:8000/tracks/1'
$Form = '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}'
Invoke-WebRequest -Method 'PUT' -Uri $Url -Body $Form -ContentType "application/json"


3:
$Url = 'http://127.0.0.1:8000/tracks/1'
Invoke-WebRequest -Method 'DELETE' -Uri $Url -ContentType "application/json"
---draft scripts:


curl -X PUT -H "Content-Type: application/json" -d '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}' http://localhost:8000/tracks/1

$Request = Invoke-WebRequest -Uri $Uri -Method Post -Form $Form
echo $Request

$Url = 'http://127.0.0.1:8000/tracks/'
$Form = '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}'
Invoke-WebRequest -Method 'Post' -Uri $Url -Body $Form -ContentType "application/json"




Invoke-WebRequest -Method 'Post' -Uri $url -Body ({"artist"= "Sonic Youth"}|ConvertTo-Json) -ContentType "application/json"

curl -X POST -H "Content-Type: application/json" -d '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}' http://localhost:8000/tracks