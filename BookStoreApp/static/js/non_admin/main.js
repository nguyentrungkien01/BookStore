$(function () {
    $('.block-product').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1400,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 800,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    //hieu ung header va nut backtotop
    $("#backtotop").click(function () {
        $("html, body").animate({
            scrollTop: 0
        }, 400);
    });

    $(window).scroll(function () {
        if ($("body,html").scrollTop() > 150) {
            $(".navbar").addClass("fixed-top");
        } else {
            $(".navbar").removeClass("fixed-top");
        }
    });

    $(window).scroll(function () {
        if ($("body,html").scrollTop() > 400) {
            $(".scroll-up").addClass("show");
        } else {
            $(".scroll-up").removeClass("show");
        }
    });

    // header form dangnhap dangky
    $(".btn-login").click(function (e) {
        $("ul.tabs .login-tab").addClass("active");
    });
    $(".btn-register").click(function (e) {
        $("ul.tabs .register-tab").addClass("active");
    });

    $("ul.tabs .login-tab").click(function (e) {
        $("ul.tabs .login-tab").addClass("active");
        $("ul.tabs .register-tab").removeClass("active");
    });

    $("ul.tabs .register-tab").click(function (e) {
        $("ul.tabs .register-tab").addClass("active");
        $("ul.tabs .login-tab").removeClass("active");
    });

    // form dangnhap dangky 
    $(".register-tab").click(function (e) {
        $('#login-form').removeClass("fade");
        $('#register-form').removeClass("fade");
        $('#login-form').modal("hide");
        $('#register-form').modal("show");
    });
    $(".login-tab").click(function (e) {
        $('#login-form').removeClass("fade");
        $('#register-form').removeClass("fade");
        $('#register-form').modal("hide");
        $('#login-form').modal("show");
    });
    $(".close").click(function (e) {
        $('.modal').addClass("fade");
        $("ul.tabs .login-tab").removeClass("active");
        $("ul.tabs .register-tab").removeClass("active");
    });

    $("#book-list-btn").click(function (e) {
        $(".category-content").toggleClass("show");
    });

    // thumb-img
    $(".thumb-img.thumb1").addClass('vienvang');
    $('.thumb-img').click(function (e) {
        $('.product-image').attr('src', this.src);
    });

    $('.thumb-img').click(function (e) {
        $('.thumb-img:not(:hover)').removeClass('vienvang');
        $(this).addClass('vienvang');
    });

    //btn-spin
    $(".btn-inc").click(function (e) {
        var strval = $(this).parent().prev().val();
        var val = parseInt(strval) + 1;
        $(this).parent().prev().attr('value', val);
    });
    $(".btn-dec").click(function (e) {
        var strval = $(this).parent().next().val();
        var val = parseInt(strval) - 1;
        if (val < 1) {
            $(this).parent().next().attr('value', 1);
        } else {
            $(this).parent().next().attr('value', val);
        }
    });

    // gui danh gia
    $(".vote-form").hide(200);
    $(".write-form").click(function (e) {
        $(".vote-form").toggle(200);
    });




    //rotate chevron
    $('#step1contentid').on('show.bs.collapse', function () {
        $(this).prev().addClass("active");
    })
    $('#step1contentid').on('hide.bs.collapse', function () {
        $(this).prev().removeClass("active");
    })
    $('#step2contentid').on('show.bs.collapse', function () {
        $(this).prev().addClass("active");
    })
    $('#step2contentid').on('hide.bs.collapse', function () {
        $(this).prev().removeClass("active");
    })
    $('#step3contentid').on('show.bs.collapse', function () {
        $(this).prev().addClass("active");
    })
    $('#step3contentid').on('hide.bs.collapse', function () {
        $(this).prev().removeClass("active");
    })

    // nut btn-shopping-without-signup
    $("#step1contentid").collapse('show');
    $(".btn-shopping-without-signup").click(function (e) {
        $("#step1contentid").collapse('hide');
        $("#step2contentid").collapse('show');
    });

    // validate
    $("#form-signup").validate({
        rules: {
            name: {
                required: true,
            },
            phone: {
                required: true,
                minlength: 8
            },
            password: {
                required: true,
                minlength: 6
            },
            confirm_password: {
                required: true,
                minlength: 6,
                equalTo: "#inputPassword"
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            name: {
                required: "Vui lòng nhập họ và tên",
            },
            phone: {
                required: "Vui lòng nhập số điện thoại",
                minlength: "Số máy quý khách vừa nhập là số không có thực"
            },
            password: {
                required: 'Vui lòng nhập mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự'
            },
            confirm_password: {
                required: 'Vui lòng nhập lại mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự',
                equalTo: 'Mật khẩu không trùng'
            },
            email: {
                required: "Vui lòng nhập email",
                minlength: "Email không hợp lệ",
                email: "Vui lòng nhập email",
            }
        }
    });

    $("#form-signin").validate({
        rules: {
            password: {
                required: true,
                minlength: 6
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            password: {
                required: 'Vui lòng nhập mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự'
            },
            email: {
                required: "Vui lòng nhập email",
                minlength: "Email không hợp lệ",
                email: "Vui lòng nhập email",
            }
        }
    });

    $("#form-signup-cart").validate({
        rules: {
            name: {
                required: true,
            },
            phone: {
                required: true,
                minlength: 8
            },
            password: {
                required: true,
                minlength: 6
            },
            confirm_password: {
                required: true,
                minlength: 6,
                equalTo: "#inputPassword"
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            name: {
                required: "Vui lòng nhập họ và tên",
            },
            phone: {
                required: "Vui lòng nhập số điện thoại",
                minlength: "Số máy quý khách vừa nhập là số không có thực"
            },
            password: {
                required: 'Vui lòng nhập mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự'
            },
            confirm_password: {
                required: 'Vui lòng nhập lại mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự',
                equalTo: 'Mật khẩu không trùng'
            },
            email: {
                required: "Vui lòng nhập email",
                minlength: "Email không hợp lệ",
                email: "Vui lòng nhập email",
            }
        }
    });

    $("#form-signin-cart").validate({
        rules: {
            password: {
                required: true,
                minlength: 6
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            password: {
                required: 'Vui lòng nhập mật khẩu',
                minlength: 'Vui lòng nhập ít nhất 6 kí tự'
            },
            email: {
                required: "Vui lòng nhập email",
                minlength: "Email không hợp lệ",
                email: "Vui lòng nhập email",
            }
        }
    });

    // add to cart 
    let product = {
        name: $('.block-info .book-name').text(),
        tag: $('.product-image').attr("alt"),
        price: parseFloat($('.price span.new-price').text()),
        old_price: parseFloat($('.price span.old-price').text()),
        inCart: 0
    }

    let carts = document.querySelector('.buy-btn');
    if (carts) {
        carts.addEventListener('click', () => {
            cartNumbers(product);
            totalCost(product);
        })
    }

    function onLoadCartNumbers() {
        let productNumbers = localStorage.getItem('cartNumbers');
        if (productNumbers) {
            document.querySelector('.cart .cart-amount').textContent = productNumbers;
        }
    }

    function cartNumbers(product) {

        let productNumbers = localStorage.getItem('cartNumbers');
        productNumbers = parseInt(productNumbers);

        if (productNumbers) {
            localStorage.setItem('cartNumbers', productNumbers + parseInt($(".amount-product").val()));
            document.querySelector('.cart .cart-amount').textContent = productNumbers + parseInt($(".amount-product").val());
        } else {
            localStorage.setItem('cartNumbers', parseInt($(".amount-product").val()));
            document.querySelector('.cart .cart-amount').textContent = parseInt($(".amount-product").val());
        }
        setItem(product);
    }

    function setItem(product) {
        let cartItems = localStorage.getItem('productsInCart');
        cartItems = JSON.parse(cartItems);

        if (cartItems != null) {
            if (cartItems[product.tag] == undefined) {
                cartItems = {
                    ...cartItems,
                    [product.tag]: product
                }
            }
            cartItems[product.tag].inCart += parseInt($(".amount-product").val());
        } else {
            product.inCart = parseInt($(".amount-product").val());
            cartItems = {
                [product.tag]: product
            }
        }

        localStorage.setItem('productsInCart', JSON.stringify(cartItems));
    }

    function totalCost(product) {
        let cartCost = localStorage.getItem('totalCost');

        if (cartCost != null) {
            cartCost = parseFloat(cartCost);
            localStorage.setItem('totalCost', cartCost + parseInt($(".amount-product").val()) * product.price);
        } else {
            localStorage.setItem('totalCost', parseInt($(".amount-product").val()) * product.price);
        }
    }

    function displayCart() {
        let cartItems = localStorage.getItem("productsInCart");
        cartItems = JSON.parse(cartItems);
        let cartContent = document.querySelector(".cart-content");
        let cartCost = localStorage.getItem('totalCost');
        let productNumbers = localStorage.getItem('cartNumbers');

        if (cartItems == null) {
            $(".cart-empty").removeClass("d-none");
            $('.cart').addClass('lock'); // test "d-none -> lock"
            $('.cart-steps').addClass('d-none');
        }
        if (cartItems && cartContent) {
            $(".cart-empty").addClass("d-none");
            $('.cart').removeClass('d-none');
            $('.cart-steps').removeClass('d-none');

            cartContent.innerHTML = '';

            cartContent.innerHTML += `
            <h6 class="cart-header">GIỎ HÀNG CỦA BẠN <span>(${productNumbers} sản phẩm)</span></h6>
            <div class="cart-list-items">
            `
            Object.values(cartItems).map(item => {
                cartContent.innerHTML += `
                    <div class="cart-item d-flex">
                        <a href="product-item.html" class="img">
                            <img src="../static/images/${item.tag}.jpg" class="img-fluid" alt="${item.tag}">
                        </a>
                        <div class="item-caption d-flex w-100">
                            <div class="item-info ml-3">
                                <a href="product-item.html" class="book-name">${item.name}</a>
                                <div class="amount d-flex">
                                    <div class="input-number input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text btn-spin btn-dec">-</span>
                                        </div>
                                        <input type="text" value="${item.inCart}" class="amount-product  text-center">
                                        <div class="input-group-append">
                                            <span class="input-group-text btn-spin btn-inc">+</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item-price ml-auto d-flex flex-column align-items-end">
                                <div class="new-price">${parseFloat(item.price).toFixed(3)} ₫</div>
                                <div class="old-price">${parseFloat(item.old_price).toFixed(3)} ₫</div>
                                <span class="remove mt-auto"><i class="far fa-trash-alt"></i></span>
                            </div>
                        </div>
                    </div>
                `
            })

            cartContent.innerHTML += `
            </div>

            <div class="row">
                <div class="col-md-3">
                    <a href="index.html" class="btn buy-more mb-3">Mua thêm</a>
                </div>
                <div class="col-md-5 offset-md-4">
                    <div class="total-price">
                        <div class="group d-flex justify-content-between">
                            <p class="label">Tạm tính:</p>
                            <p class="tamtinh">${parseFloat(cartCost).toFixed(3)} ₫</p>
                        </div>
                        <div class="group d-flex justify-content-between">
                            <p class="label">Giảm giá:</p>
                            <p class="giamgia">0 ₫</p>
                        </div>
                        <div class="group d-flex justify-content-between">
                            <p class="label">Phí vận chuyển:</p>
                            <p class="phivanchuyen">0 ₫</p>
                        </div>
                        <div class="group d-flex justify-content-between">
                            <p class="label">Phí dịch vụ:</p>
                            <p class="phidicvu">0 ₫</p>
                        </div>
                        <div class="group d-flex justify-content-between align-items-center">
                            <strong class="text-uppercase">Tổng cộng:</strong>
                            <p class="total">${parseFloat(cartCost).toFixed(3)} ₫</p>
                        </div>
                        <small class="note d-flex justify-content-end text-muted">
                            (Giá đã bao gồm VAT)
                        </small>
                    </div>
                </div>
            </div>
            `

        }
    }

    $(".btn-checkout").click(function (e) {
        localStorage.clear();
        location.reload(true);
        alert("cảm ơn đã mua hàng");
    });

    onLoadCartNumbers();
    displayCart()

    $('.items .row').isotope({
        itemSelector: '.item',
    })

    $('.tag a').click(function (e) {
        var author = $(this).data('author');

        if (author == 'all') {
            $('.items .row').isotope({
                filter: '*'
            })
        } else {
            $('.items .row').isotope({
                filter: author
            });
        }
        return false;
    });

    $('.thay-doi-mk').hide();
    $("#changepass").click(function (e) {
        $('.thay-doi-mk').toggle(200);
    });

});

// init cursor
var cursors = [{
    cursor_id: "3",
    cursor_type: "0",
    cursor_shape: "15",
    cursor_image: "",
    default_cursor: "auto",
    hover_effect: "plugin",
    body_activation: "1",
    element_activation: "0",
    selector_type: "tag",
    selector_data: "body",
    color: "#cc3a3b",
    width: "30",
    blending_mode: "normal"
}];

   $('#form-signup').on('submit', function(e) {
    e.preventDefault(); // Now nothing will happen
});