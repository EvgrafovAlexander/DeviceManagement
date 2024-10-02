# stdlib
import uuid

# thirdparty
from sqlalchemy import select, update

# project
from src.management.models import CommandLog
from src.management.schemas import Command
from src.utils.repository import BaseRepository


class CommandLogRepository(BaseRepository):
    model = CommandLog

    async def log_sending_command(self, device_id: uuid.UUID, send_command: Command) -> bool:
        log_row = self.model(
            device_id=device_id,
            command=send_command.command,
            params=send_command.params,
        )
        self.session.add(log_row)
        await self.session.commit()
        return True
