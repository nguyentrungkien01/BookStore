from BookStoreApp import db
from BookStoreApp.model.account_model import AccountModel
from BookStoreApp import CustomerModel, RoleModel

def get_info_user_by_account_id(id=0):
    query = db.session.query(AccountModel.last_name, AccountModel.first_name, AccountModel.avatar,\
                            AccountModel.joined_date, CustomerModel.phone_number,CustomerModel.date_of_birth,\
                            CustomerModel.gmail,  AccountModel.type, RoleModel.name, CustomerModel.address,\
                             CustomerModel.district, CustomerModel.city, AccountModel.username)\
            .filter(AccountModel.role_id == RoleModel.role_id)\
            .filter(AccountModel.account_id == id)
    return query.first()