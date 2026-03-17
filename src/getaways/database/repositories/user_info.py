from src.core.gateways.database.repositories.base_repository import BaseRepository
from src.domain.dto.base import UserInfoBaseSchema
from src.domain.interfaces.gateways.database.repositories.user_info_repository import IUserInfoRepository


class UserInfoRepository(BaseRepository, IUserInfoRepository):
    table_name = "user_info"
    schema: type[UserInfoBaseSchema]
