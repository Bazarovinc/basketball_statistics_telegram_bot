from src.core.gateways.database.unit_of_work.base import BaseUnitOfWork
from src.domain.interfaces.gateways.database.repositories import IUserAgreementRepository, IUserRepository


class UserServiceBaseUnitOfWork(BaseUnitOfWork):
    user_repo: IUserRepository
    user_agreement_repo: IUserAgreementRepository
