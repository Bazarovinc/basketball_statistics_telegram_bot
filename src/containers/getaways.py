from dependency_injector import containers, providers

from src.getaways.image_loader import ImageLoaderClient
from src.getaways.league_reader import LeagueReader
from src.getaways.object_storage_client import ObjectStorageClient
from src.settings.object_storage import ObjectStorageSettings


class GetawaysContainer(containers.DeclarativeContainer):
    image_loader = providers.Singleton(ImageLoaderClient)
    league_reader = providers.Singleton(LeagueReader)
    object_storage_settings = providers.Singleton(ObjectStorageSettings)
    object_storage_client = providers.Singleton(
        ObjectStorageClient,
        settings=object_storage_settings,
    )