from BookStoreApp.repository.admin.profile_repository import get_info_user_by_account_id as giu

def get_info_user_by_account_id(id=0):
    if id:
        return giu(id)

# Chuyển thông tin sang dictionary
def get_info(data=None, **kwargs):
    if data is None:
        return []

    profile_data = []

    profile_data.append({
        'last_name': data[0],
        'first_name': data[1],
        'avatar': data[2],
        'joined_date': data[3].strftime('%d/%m/%Y'),
        'phone_number': data[4],
        'date_of_birth': data[5].strftime('%d/%m/%Y'),
        'gmail': data[6],
        'type': data[7],
        'role_name': data[8],
        'address': data[9] + ", " + data[10] + ", " + data[11],
        'username': data[12]
    })

    return profile_data
