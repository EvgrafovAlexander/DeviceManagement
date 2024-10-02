# stdlib
import uuid

# thirdparty
from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# project
from src.database import CustomBase


class DeviceType(CustomBase):
    __tablename__ = "device_types"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Group id"
    )
    description = Column(String, doc="Group description")

    devices = relationship("Device", back_populates="type", cascade="all, delete-orphan")


class Device(CustomBase):
    __tablename__ = "devices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Id")
    group_id = Column(UUID(as_uuid=True), ForeignKey("device_types.id"))
    house_id = Column(UUID(as_uuid=True), ForeignKey("houses.id"))
    serial_number = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Serial number")
    status = Column(Boolean, default=False, doc="On/Off")

    type = relationship("DeviceType", back_populates="devices")
