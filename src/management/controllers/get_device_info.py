# stdlib
import uuid
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.device import DeviceRepository
from src.management.schemas import DeviceInfo
from src.utils.controller import AsyncController


class GetDeviceInfoController(AsyncController):
    def __init__(self, device_id: uuid.UUID, session: AsyncSession):
        self.device_id = device_id
        self.session = session

    async def __call__(self, *args, **kwargs) -> DeviceInfo:
        try:
            logger.info("GetDeviceInfoController, device_id: %s" % self.device_id)
            device_info = await DeviceRepository(session=self.session).get_device_info(self.device_id)
            return DeviceInfo(
                id=device_info.id,
                group_id=device_info.group_id,
                house_id=device_info.house_id,
                serial_number=device_info.serial_number,
                status=device_info.status,
            )
        except Exception as e:
            logger.error("GetDeviceInfoController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"GetDeviceInfoController Error, detail: {e}",
            )
