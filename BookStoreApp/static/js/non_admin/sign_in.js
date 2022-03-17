$('#btnSignIn').click(function () {
    if (isExactlyDataSignIn() == true) {
        fetch('/client/api/sign-in', {
            method: 'post',
            body: JSON.stringify({
                'username': document.getElementById('usernameSignIn').value,
                'password': document.getElementById('passwordSignIn').value
            }),
            headers: {
                'Accept': 'application/json',
                'Context-Type': 'application/json',
            }
        }).then(res => res.json()).then(data => {
            if (data == 'error') {
                Swal.fire({
                    title: 'Tên đăng nhập hoặc mật khẩu sai !',
                    text: 'Xin vui lòng kiểm tra lại',
                    icon: 'warning',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Ok',
                })
            } else
                window.location = "/"
        })
    }
})

// kiểm tra thông tin nhập
function isExactlyDataSignIn() {
    if (document.getElementById('usernameSignIn').value == '' || document.getElementById('passwordSignIn').value == '') {
        Swal.fire({
            title: 'Vui lòng kiểm tra lại !!!',
            text: '',
            icon: 'warning',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Ok',
        })
        return false
    }
    return true
}