import json
import pathlib
from typing import List, Union

from fastapi import FastAPI, Response

from models import Track

app = FastAPI()

data = []

@app.on_event("startup")
async def startup_event():
    datapath = pathlib.Path() / 'data' / 'tracks.json'
    with open (datapath, 'r') as f:
        tracks = json.load(f)
        for track in tracks:
            data.append(Track(**track).dict())
    
@app.get('/tracks/', response_model=List[Track])
def tracks():
    return data

@app.get('/tracks/{track_id}', response_model=Union[Track,str])
def tracks(track_id: int, response: Response):
    track = None
    for t in data:
        if t['id'] == track_id:
            track = t
            break
    if track is None:
        response.status_code = 404
        return "Track not found"
    return track

@app.post('/tracks/', response_model=Track, status_code = 201)
def create_track(track:Track):
    track_dict = track.dict()
    track_dict['id'] = max(data, key=lambda x: x['id']).get('id') + 1
    data.append(track_dict)
    return track_dict
                           