# stdlib
import uuid
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.management.repositories.command_log import CommandLogRepository
from src.management.schemas import UpdateResult, Command
from src.utils.controller import AsyncController


class SendCommandToDeviceController(AsyncController):
    def __init__(self, device_id: uuid.UUID, send_command: Command, session: AsyncSession):
        self.device_id = device_id
        self.send_command = send_command
        self.session = session

    async def __call__(self, *args, **kwargs) -> UpdateResult:
        try:
            logger.info("SendCommandToDeviceController, device_id: %s" % self.device_id)
            is_created = await CommandLogRepository(session=self.session).log_sending_command(
                self.device_id, self.send_command,
            )
            """
            ...Код отправки команды на устройство...
            """
            return UpdateResult(
                success=is_created,
            )
        except Exception as e:
            logger.error("SendCommandToDeviceController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"SendCommandToDeviceController Error, detail: {e}",
            )
