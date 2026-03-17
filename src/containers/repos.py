from dependency_injector import containers, providers

from src.core.gateways.database.session import get_pool
from src.getaways.database.unit_of_work import FullStatisticsSaverUnitOfWork, UserServiceUnitOfWork


class ReposContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    pool = providers.Factory(get_pool, postgres_settings=config)

    user_service_uow = providers.Factory(UserServiceUnitOfWork, pool=pool)
    full_statistics_saver_uow = providers.Factory(FullStatisticsSaverUnitOfWork, pool=pool)