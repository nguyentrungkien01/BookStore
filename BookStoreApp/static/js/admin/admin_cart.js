window.onload = function() {
    var x = location.href;
    if (x.indexOf("admin/cartview") != -1){
        passCartData();
    }
}

function passCartData() {
    fetch('/admin/api/cart', {
        method: 'post',
        body: JSON.stringify({
        }),
        headers: {
          'Accept': 'application/json',
            'Context-Type': 'application/json',
        }
    }).then(
    res => {
        if (res) {
            if (res?.status === 200) {
                console.log("Thao tác thành công")
                console.log("res", res)
                return res.text()
            }
            else {
                console.log("Thao tác thất bại", res?.statusText)
            }
        }
    }).then(datas => {

            add_child();
    }).catch(err => {
        console.log(err);
    });
}

function add_child() {
       //tạo phần tử p
       var p = document.createElement("p");

       //tạo phần tử text
       var node = document.createTextNode("Some new text");

       //gắn node vào p
       p.appendChild(node);

       //Thay đổi một số thuộc tính của p
       p.appendChild(node);


       var div = document.getElementById("demo");
       //gắn p vào div
       div.appendChild(p);
   }