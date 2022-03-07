from BookStoreApp import  app
from BookStoreApp.service.admin.account_service import get_account as ga, set_change_passwork as scp

def change_passwork(new_password=None, account=None):
    if new_password and account:
        scp(new_password=new_password, account=account)

def get_account(username=None, password=None):
    return ga(username=username, password=password)