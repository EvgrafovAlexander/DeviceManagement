# stdlib
import uuid
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.device import DeviceRepository
from src.management.schemas import DeviceInfo, UpdateStatus, UpdateResult
from src.utils.controller import AsyncController


class UpdateDeviceStatusController(AsyncController):
    def __init__(self, device_id: uuid.UUID, update_status: UpdateStatus, session: AsyncSession):
        self.device_id = device_id
        self.update_status = update_status
        self.session = session

    async def __call__(self, *args, **kwargs) -> UpdateResult:
        try:
            logger.info("UpdateDeviceStatusController, device_id: %s" % self.device_id)
            is_updated = await DeviceRepository(session=self.session).update_device_status(
                self.device_id, self.update_status.status
            )
            return UpdateResult(
                success=is_updated,
            )
        except Exception as e:
            logger.error("UpdateDeviceStatusController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"UpdateDeviceStatusController Error, detail: {e}",
            )
