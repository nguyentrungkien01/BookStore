// Lấy thông tin người dùng
function getProfileData(account_id){
    fetch('/admin/api/profile', {
        method: 'post',
        body: JSON.stringify({
            'account_id':account_id
        }),
        headers: {
          'Accept': 'application/json',
            'Context-Type': 'application/json',
        }
    }).then(res => res.json()).then(data => {
            setProfileData(data[0])
    }).catch(err => {
        console.log(err)
    });
}

// Gán dữ liệu ra html
function setProfileData(data){
    document.getElementById('lastName').innerHTML = data['last_name']
    document.getElementById('firstName').innerHTML = data['first_name']
    document.getElementById('dateOfBirth').innerHTML = data['date_of_birth']
    document.getElementById('joinedDate').innerHTML = data['joined_date']
    document.getElementById('phoneNumber').innerHTML = data['phone_number']
    document.getElementById('gmail').innerHTML = data['gmail']
    document.getElementById('address').innerHTML = data['address']
    document.getElementById('avatar').src = data['avatar']
    document.getElementById('username').innerHTML = data['username']
    document.getElementById('role').innerHTML = data['role_name']
}