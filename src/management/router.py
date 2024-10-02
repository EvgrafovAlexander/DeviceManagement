# stdlib
import uuid

# thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import get_db_session
from src.management.controllers.get_device_info import GetDeviceInfoController
from src.management.controllers.send_command_to_device import SendCommandToDeviceController
from src.management.controllers.update_device_status import UpdateDeviceStatusController
from src.management.schemas import DeviceInfo, UpdateStatus, UpdateResult, Command

router = APIRouter(prefix="/devices", tags=["devices"])


@router.get("/{device_id}", response_model=DeviceInfo)
async def get_device_info(
    device_id: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
):
    """Получает подробную информацию об устройстве по его ID"""
    return await GetDeviceInfoController(device_id, session)()


@router.put("/{device_id}/status", response_model=UpdateResult)
async def update_device_status(
    device_id: uuid.UUID,
    update_status: UpdateStatus,
    session: AsyncSession = Depends(get_db_session),
):
    """Обновляет состояние устройства"""
    return await UpdateDeviceStatusController(device_id, update_status, session)()


@router.put("/{device_id}/commands")
async def send_command_to_device(
    device_id: uuid.UUID,
    send_command: Command,
    session: AsyncSession = Depends(get_db_session),
):
    """Обновляет состояние устройства"""
    return await SendCommandToDeviceController(device_id, send_command, session)()
