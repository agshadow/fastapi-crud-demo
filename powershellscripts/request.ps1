$Uri = 'http://127.0.0.1:8000/tracks/1'
$Form = ${
    artist= "Sonic Youth"
    title= "Silver Rocket"
    last_play= "2017-10-18 15:15:26"
    duration= 200
}

$Request = Invoke-WebRequest -Uri $Uri -Method Post -Form $Form
echo $Request