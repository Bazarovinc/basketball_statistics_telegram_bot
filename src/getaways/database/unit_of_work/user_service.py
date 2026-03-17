from src.domain.interfaces.gateways.database.unit_of_work import UserServiceBaseUnitOfWork
from src.getaways.database.repositories import UserAgreementRepository
from src.getaways.database.repositories.user import UserRepository


class UserServiceUnitOfWork(UserServiceBaseUnitOfWork):
    user_repo: UserRepository
    user_agreement_repo: UserAgreementRepository
