//window.onload = function() {
//    var x = location.href;
//    if (x.indexOf("admin/cartview") != -1){
//        passCartData();
//    }
//}
//
//function passCartData() {
//    fetch('/admin/api/cart', {
//        method: 'post',
//        body: JSON.stringify({
//        }),
//        headers: {
//          'Accept': 'application/json',
//            'Context-Type': 'application/json',
//        }
//    }).then(
//    res => {
//        if (res) {
//            if (res?.status === 200) {
//                console.log("Thao tác thành công")
//                console.log("res", res)
//                return res.text()
//            }
//            else {
//                console.log("Thao tác thất bại", res?.statusText)
//            }
//        }
//    }).then(datas => {
//        alert("thanh cong");
//
//    }).catch(err => {
//        console.log(err);
//    });
//}