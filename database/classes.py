import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import types, String, types

import uuid


class Base(DeclarativeBase):
    pass


class SongsCurrent(Base):
    __tablename__ = 'SONGS_CURRENT'

    song_id: Mapped[uuid.UUID] = mapped_column(
        types.UUID,
        primary_key=True,
        default=uuid.uuid4)
    url: Mapped[str] = mapped_column(String)


class MusicCurrent(Base):
    __tablename__ = 'MUSIC_CURRENT'

    song_id: Mapped[uuid.UUID] = mapped_column(
        types.UUID,
        primary_key=True,
        default=uuid.uuid4)
    artist_id: Mapped[str] = mapped_column(String)


class Artist(Base):
    __tablename__ = 'ARTIST'

    artist_id: Mapped[uuid.UUID] = mapped_column(
        types.UUID,
        primary_key=True,
        default=uuid.uuid4)
    artist_name: Mapped[str] = mapped_column(String)
    artist_genre: Mapped[str] = mapped_column(String)
