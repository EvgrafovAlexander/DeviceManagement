# stdlib
import uuid

# thirdparty
from sqlalchemy import Boolean, Column, String, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# project
from src.database import CustomBase


class User(CustomBase):
    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="User id"
    )
    name = Column(String, doc="User name")
    email = Column(String, doc="User e-mail")

    houses = relationship("House", back_populates="user", cascade="all, delete-orphan")


class House(CustomBase):
    __tablename__ = "houses"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="House id"
    )
    address = Column(String, doc="Address")
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="houses")


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


class CommandLog(CustomBase):
    __tablename__ = "command_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Log id")
    device_id = Column(UUID(as_uuid=True))
    command = Column(String, doc="Device command")
    params = Column(String, doc="Command parameters")
    timestamp = Column(DateTime, server_default=func.now())
