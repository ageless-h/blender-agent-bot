from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Position3D(BaseModel):
    x: float
    y: float
    z: float


class Rotation3D(BaseModel):
    x: float
    y: float
    z: float


class Scale3D(BaseModel):
    x: float
    y: float
    z: float


class Color(BaseModel):
    r: float = Field(ge=0.0, le=1.0)
    g: float = Field(ge=0.0, le=1.0)
    b: float = Field(ge=0.0, le=1.0)
    a: float = Field(default=1.0, ge=0.0, le=1.0)


class MaterialRef(BaseModel):
    name: str
    slot_index: int | None = None
    library: str | None = None


class ObjectInfo(BaseModel):
    name: str
    type: str
    location: Position3D | None = None
    rotation: Rotation3D | None = None
    scale: Scale3D | None = None
    visible: bool = True
    selected: bool = False
    materials: list[MaterialRef] = Field(default_factory=list)


class SceneInfo(BaseModel):
    name: str
    frame_start: int
    frame_end: int
    frame_current: int
    fps: float
    object_count: int = 0
    active_object: str | None = None


class ViewportCapture(BaseModel):
    data_base64: str
    mime_type: str = "image/png"
    width: int
    height: int
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


__all__ = [
    "ObjectInfo",
    "SceneInfo",
    "ViewportCapture",
    "Position3D",
    "Rotation3D",
    "Scale3D",
    "Color",
    "MaterialRef",
]
