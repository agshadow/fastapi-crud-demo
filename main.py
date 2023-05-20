import json
import pathlib
from typing import List, Union

from fastapi import FastAPI, Response, Depends


from sqlmodel import Session, select

from database import TrackModel, engine, create_tables, delete_database

from models import Track

app = FastAPI()

data = []


@app.on_event("startup")
async def startup_event():
    datapath = pathlib.Path() / "data" / "tracks.json"

    result = None
    with Session(engine) as session:
        stmt = select(TrackModel)
        result = session.exec(stmt).first()

    if result is None:
        print("loading json")

        with Session(engine) as session1:
            with open(datapath, "r") as f:
                tracks = json.load(f)
                for track in tracks:
                    session.add(TrackModel(**track))
            session.commit()
    else:
        print("data already loded")


# get_session dependency
def get_session():
    with Session(engine) as session:
        yield session


@app.get("/tracks/", response_model=List[Track])
def tracks(session: Session = Depends(get_session)):
    result = None
    stmt = select(TrackModel)
    result = session.exec(stmt).all()
    print("returning result")
    return result


@app.get("/tracks/{track_id}", response_model=Union[Track, str])
def tracks(track_id: int, response: Response, session: Session = Depends(get_session)):
    result = None
    stmt = select(TrackModel).where(TrackModel.id == track_id)
    track = session.exec(stmt).first()
    print("returning result", track)
    if track is None:
        response.status_code = 404
        return "Track not found"
    return track


@app.post("/tracks/", response_model=Track, status_code=201)
def create_track(track: TrackModel, session: Session = Depends(get_session)):
    session.add(track)
    session.commit()
    session.refresh(track)
    return track


@app.put("/tracks/{track_id}", response_model=Union[Track, str])
def tracks(
    track_id: int,
    updated_track: TrackModel,
    response: Response,
    session: Session = Depends(get_session),
):
    track = None
    track = session.exec(select(TrackModel).where(TrackModel.id == track_id)).first()

    if track is None:
        response.status_code = 404
        return "Track not found"
    track_dict = updated_track.dict(exclude_unset=True)
    for key, val in track_dict.items():
        setattr(track, key, val)
    session.add(track)
    session.commit()
    session.refresh(track)
    return track


@app.delete("/tracks/{track_id}")
def tracks(
    track_id: int,
    response: Response,
    session: Session = Depends(get_session),
):
    track = session.get(TrackModel, track_id)
    if track is None:
        response.status_code = 404
        print("track not founddddd")
        return "Track not found"

    session.delete(track)
    session.commit()
    return Response(status_code=200)
