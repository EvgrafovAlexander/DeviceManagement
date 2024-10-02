# stdlib
import uuid

# thirdparty
from sqlalchemy import select, update

# project
from src.management.models import Device
from src.utils.repository import BaseRepository


class DeviceRepository(BaseRepository):
    model = Device

    async def get_device_info(self, device_id: uuid.UUID):
        query: str = select(self.model).filter(self.model.id == str(device_id))
        device_raw = await self.session.execute(query)
        device = device_raw.scalar()
        return device

    async def update_device_status(self, device_id: uuid.UUID, status: bool) -> bool:
        query: str = (
            update(self.model)
            .where(self.model.id == str(device_id))
            .values(
                status=status,
            )
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.rowcount > 0
