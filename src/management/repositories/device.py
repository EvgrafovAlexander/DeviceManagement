# stdlib
from uuid import UUID

# project
from src.management.models import Device
from src.utils.repository import BaseRepository


class DeviceRepository(BaseRepository):
    model = Device

    async def get_device_info(self, device_id: int) -> dict:
        return {}
