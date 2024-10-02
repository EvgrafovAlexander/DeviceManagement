# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.device import DeviceRepository
from src.utils.controller import AsyncController


class GetDeviceInfoController(AsyncController):
    def __init__(self, device_id: int, session: AsyncSession):
        self.device_id = device_id
        self.session = session

    async def __call__(self, *args, **kwargs) -> dict:
        try:
            logger.info("GetDeviceInfoController, device_id: %s" % self.device_id)
            info = await DeviceRepository(session=self.session).get_device_info(self.device_id)
            return info
        except Exception as e:
            logger.error("GetDeviceInfoController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"GetDeviceInfoController Error, detail: {e}",
            )
