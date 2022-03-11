var val =0
window.onload = function() {
    var x = location.href
    if (x.indexOf('admin/cartview') != -1){
        getCartData()
    }
}

// gửi thông tin lên server
function getCartData(){
    val = getPriceRange()
    setDeleteData()
    fetch('/admin/api/cart', {
        method: 'post',
        body: JSON.stringify({
            'typeArrange': getTypeArrange()
        }),
        headers: {
          'Accept': 'application/json',
            'Context-Type': 'application/json',
        }
    }).then(res => res.json()).then(data => {
            if (getTypeArrange() == 0 && val ==0)           // sắp xếp mặc định
                setCartData(data[0], data[1])
            else if ( val ==0)
                setCartDataArrange(data[0], data[1], data[2])
                else
                      setCartByPrice(data[0], data[1], data[2])

//            alert(data[0][i]['username'] + " - " + data[0][i]['phone_number'])
    }).catch(err => {
        console.log(err)
    });
}
// Đưa dữ liệu lên client
function setCartData(cart, book){
    var cartId = 1
    for(let i =0; i < cart.length; i++){
        var parent = `<div id='c${cartId}' class='cart-id'></div>`
        document.getElementById('cart-admin').insertAdjacentHTML('beforeend', parent)

        var child =     `<div class="info-user">
                            <div>${cartId}. Tên tài khoản: ${cart[i]['username']}</div>
                            <div>Họ tên: ${cart[i]['last_name']} ${cart[i]['first_name']}</div>
                            <div>Số điện thoại: ${cart[i]['phone_number']}</div>
                            <div>Tổng tiền: ${format(cart[i]['total_money'])}</div>
                         </div>`
        ci = 'c'+(cartId).toString();
        document.getElementById(ci).insertAdjacentHTML('afterbegin', child)

        var bookId =1
        var bookx = ``
        var listBook = `<div id='b${cartId++}' class='list-book'></div>`
        document.getElementById(ci).insertAdjacentHTML('beforeend', listBook)
        for(let j = 0; j <book.length; j++){
            if(cart[i]['cart_id'] == book[j]['cart_id']){
                bookx += `<div class="book">
                                <div>${bookId++}. ${book[j]['name_book']}</div>
                                <div><img  style='width: 50px' src='${book[j]['image']}'></div>
                                <div>Loại sách: ${book[j]['name_category']}</div>
                                <div>Số quyển: ${book[j]['amount']}</div>
                                <div>Thành tiền: ${format(book[j]['money'])}</div>
                            </div>`
            }

            if ((j == book.length-1) && (bookx !=``)){
                bi = 'b'+(cartId-1).toString()
                document.getElementById(bi).insertAdjacentHTML('afterbegin', bookx)
            }
        }
    }

}

// sắp xếp tăng/ giảm dần
function setCartDataArrange(cart, book, listTotal){
    var cartId = 1
    for(let i = 0; i < listTotal.length; i++){
        for(let c = 0; c < cart.length; c++){
            if(cart[c]['total_money'] == listTotal[i]){
                var parent = `<div id='c${cartId}' class='cart-id'></div>`
                document.getElementById('cart-admin').insertAdjacentHTML('beforeend', parent)

                var child =     `<div class='info-user'>
                                    <div>${cartId}. Tên tài khoản: ${cart[c]['username']}</div>
                                    <div>Họ tên: ${cart[c]['last_name']} ${cart[c]['first_name']}</div>
                                    <div>Số điện thoại: ${cart[c]['phone_number']}</div>
                                    <div>Tổng tiền: ${format(cart[c]['total_money'])}</div>
                                 </div>`
                ci = 'c'+(cartId).toString()
                document.getElementById(ci).insertAdjacentHTML('afterbegin', child)

                var bookId =1
                var bookx = ``
                var listBook = `<div id='b${cartId++}' class='list-book'></div>`
                document.getElementById(ci).insertAdjacentHTML('beforeend', listBook)
                for(let j = 0; j <book.length; j++){
                    if(cart[c]['cart_id'] == book[j]['cart_id']){
                        bookx += `<div class='book'>
                                        <div>${bookId++}. ${book[j]['name_book']}</div>
                                        <div><img  style='width: 50px' src='${book[j]['image']}'></div>
                                        <div>Loại sách: ${book[j]['name_category']}</div>
                                        <div>Số quyển: ${book[j]['amount']}</div>
                                        <div>Thành tiền: ${format(book[j]['money'])}</div>
                                    </div>`
                    }

                    if ((j == book.length-1) && (bookx !=``)){
                        bi = 'b'+(cartId-1).toString()
                        document.getElementById(bi).insertAdjacentHTML('afterbegin', bookx)
                    }
                }
            }
        }
    }
}

// Xóa
function setDeleteData(){
    $('div').remove('.cart-id')
}

// Qui ước sắp xếp
function getTypeArrange(){
    if (document.getElementById('input-asc').checked)  // sắp xếp tăng dần
        return 1
    if (document.getElementById('input-desc').checked) // sắp xếp giảm dần
        return -1
    else                                                // mặc định
        return 0
}

function getPriceRange(){
    if (document.getElementById('select-val').value != 'select-all')
        if(document.getElementById('select-val').value == 'select-1')       // duoi 1 trieu
            return 1
        else if (document.getElementById('select-val').value == 'select-2') // tu 1 - 2 trieu
               return 2
               else return 3                                                // tren 2 trieu
    else return 0                                                           // mac dinh
}

// Lọc danh sách từ mảng
function getListCart(list){
    let listRemove = []
    for(let i =0; i < list.length; i ++){
        if(val== 1 && list[i] > 1000000){
            listRemove.push(list[i])
        }
        if(val== 2 && (list[i] < 1000000 || list[i] > 2000000)){
            listRemove.push(list[i])
        }
        if(val== 3 && list[i] < 2000000){
            listRemove.push(list[i])
        }
    }
    for(let i =0; i < listRemove.length; i ++){
        list.splice(list.indexOf(listRemove[i]), 1)
    }

    return list;
}

// Sắp xếp theo giá
function setCartByPrice(cart, book, listTotal){
    if(listTotal.length != 0)
        setCartDataArrange(cart, book, getListCart(listTotal))
}

// format theo tiền tệ(VNĐ)
function format(n) {
    return   n.toFixed(0).replace(/./g, function(c, i, a) {
        return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "," + c : c
    }) + ' VNĐ'
}
