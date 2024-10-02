# stdlib
from uuid import UUID

# thirdparty
from pydantic import BaseModel, Field


class DeviceInfo(BaseModel):
    """Модель информации об устройстве"""

    id: UUID = Field(title="Device id")
    group_id: UUID = Field(title="Group id")
    house_id: UUID = Field(title="House id")
    serial_number: UUID = Field(title="Serial number")
    status: bool = Field(title="On/Off")
