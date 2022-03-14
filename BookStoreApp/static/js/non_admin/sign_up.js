let listCountry = {};
// Lấy dữ liệu
window.onload = function () {
    fetch("https://provinces.open-api.vn/api/?depth=2")
    .then(res => res.json())
    .then(data => {
        listCountry = data
        getCountry(data)
    }).catch(err => {
                console.log(err)
    });
}
// Đổ dữ liệu tỉnh/thành ra client
function getCountry(data){
    let options = ``
    for(let c = 0; c < data.length; c++){
        options += `<option id='${data[c].codename}' >${data[c].name}</option>`
        }
    document.getElementById('city').insertAdjacentHTML('beforeend', options)

}
// Đổ dữ liệu quận/ huyện
function setDistricts(){
    $("#district option[value='districtOption']").remove();
    let district = getCountryDataByValue()
    console.log(district)
    let options = ``
    if(district != null)
        for(let i= 0; i < district.length; i++){
            options += `<option value="districtOption" class="flag">${district[i].name}</option>`
        }
    document.getElementById('district').insertAdjacentHTML('beforeend', options)
}
// Lấy danh sách cái quận/huyện
function getCountryDataByValue(){
    for(let i =0; i< listCountry.length; i++){
            if(document.getElementById('city').value == listCountry[i].name)
                return listCountry[i].districts
    }
    return null
}

// Đăng ký tài khoản
function setSignup(){                                       // tạm thời bằng 1
    if (($("#form-signup label[class='error']").length-$("#form-signup label[style='display: none;']").length)==1 ){
        fetch('/client/sign-up/api', {
            method: 'post',
            body: JSON.stringify({

            }),
            headers: {
                'Accept': 'application/json',
                'Context-Type': 'application/json',
            }
        }).then(res => res.json()).then(data => {

        }).catch(err => {
            console.log(err)
        });
    }
}
