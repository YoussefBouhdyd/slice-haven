let countExistOrder = 0;
let total = 0;

const getCurrentDate = () => {
    const today = new Date();
    const day = String(today.getDate()).padStart(2, '0'); 
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const year = today.getFullYear();
    return `${day}/${month}/${year}`;
};

function updateTotal (newTotal){
    document.querySelector(".total").firstElementChild.innerHTML = `TOTAL:  ${newTotal} MAD`;
}

document.querySelectorAll(".file-upload").forEach((element) => {
    element.addEventListener("change",function() {
        const fileName = this.files.length > 0 ? this.files[0].name : '';
        this.nextElementSibling.innerHTML = fileName;
        if (fileName !== "") {
            this.nextElementSibling.style.padding  = "10px";
            this.nextElementSibling.style.border  = "1px dashed #333"
        }
    })
})

document.querySelectorAll(".on-click").forEach((element) => {
    element.addEventListener("click",function() {
        this.parentElement.nextElementSibling.style.display = "flex";
        this.parentElement.style.display = "none";
    })
})

document.querySelectorAll(".cancel-button").forEach((element) => {
    element.addEventListener("click",function () {
        this.parentElement.style.display = "none";
        this.parentElement.previousElementSibling.style.display = "flex"
    })
})

document.querySelectorAll(".add-button").forEach((element) => {
    element.addEventListener("click",function(){
        // add number to icon
        document.querySelector(".cart-quantity").innerHTML ++;
        // remove the label of no order
        document.querySelector(".no-order").style.display = "none"
        // ---
        this.previousElementSibling.style.display = "flex";
        this.style.display = "none";
        this.previousElementSibling.querySelector(".count-of-item").innerHTML = 1;
        // add to total 
        total += parseInt(this.parentElement.previousElementSibling.lastElementChild.textContent)
        updateTotal(total);
    })
})

document.querySelectorAll(".add-to-cart").forEach(element => {
    element.addEventListener("click",function() {
        this.previousElementSibling.innerHTML ++
        // add to total
        total += parseInt(this.parentElement.parentElement.previousElementSibling.lastElementChild.textContent);
        updateTotal(total);
    })
}
)

document.querySelectorAll(".remove-from-cart").forEach(element => {
    element.addEventListener("click",function() {
        this.nextElementSibling.innerHTML --
        if (this.nextElementSibling.innerHTML == 0){
            this.parentElement.style.display = "none";
            this.parentElement.nextElementSibling.style.display = "flex";
            // make the p.no-order displayed block
            let product =  this.parentElement.parentElement.previousElementSibling.firstElementChild.textContent;
            for (let i = 0 ; i < document.querySelector(".orders").children.length ; ++i){
                if (document.querySelector(".orders").children[i].firstElementChild.textContent === product){
                    document.querySelector(".orders").children[i].remove()
                }
            }
            countExistOrder --;
            if (countExistOrder === 0) {
                document.querySelector(".no-order").style.display = "block";
            }
            // distract 1 from icon cart
            document.querySelector(".cart-quantity").innerHTML --;
        }
        // make the number in the cart less
        let productName = this.parentElement.parentElement.previousElementSibling.firstElementChild.textContent;
        for (let i = 0 ; i < document.querySelector(".orders").children.length ; ++i){
            if (document.querySelector(".orders").children[i].firstElementChild.textContent === productName){
                let countProduct = document.querySelector(".orders").children[i].lastElementChild.textContent.slice(1);
                document.querySelector(".orders").children[i].lastElementChild.innerHTML = `<span>&times;</span> ${--countProduct}`
            }
        }
        // remove from total
        total -= parseInt(this.parentElement.parentElement.previousElementSibling.lastElementChild.textContent);
        updateTotal(total);
    })
}
)

document.querySelectorAll(".add-button").forEach((element) => {
    element.addEventListener("click",function() {
        let product = this.parentElement.previousElementSibling.firstElementChild.textContent;
        let unitPrice = this.parentElement.previousElementSibling.lastElementChild.textContent;
        let unitePriceHolder = document.createElement("span");
        unitePriceHolder.append(unitPrice);
        let orderHolder = document.createElement("div");
        orderHolder.classList.add("order");
        let productName = document.createTextNode(product);
        let nameHolder =  document.createElement("h4");
        nameHolder.classList.add("product-name");
        nameHolder.append(productName);
        let quantHolder =  document.createElement("span");
        quantHolder.classList.add("product-quantity");
        quantHolder.innerHTML = `<span>&times;</span> 1`;
        countExistOrder ++ ;
        orderHolder.append(nameHolder);
        orderHolder.append(unitePriceHolder);
        orderHolder.append(quantHolder);
        document.querySelector(".orders").append(orderHolder);
    })
})

document.querySelectorAll(".add-to-cart").forEach(element => {
    element.addEventListener("click",function() {
        let productName = this.parentElement.parentElement.previousElementSibling.firstElementChild.textContent;
        for (let i = 0 ; i < document.querySelector(".orders").children.length ; ++i){
            if (document.querySelector(".orders").children[i].firstElementChild.textContent === productName){
                let countProduct = document.querySelector(".orders").children[i].lastElementChild.textContent.slice(1);
                document.querySelector(".orders").children[i].lastElementChild.innerHTML = `<span>&times;</span> ${++countProduct}`
            }
        }
    })
})

document.querySelector(".cart").firstElementChild.onclick = function() {
    document.getElementsByClassName("command")[0].style.display = "block"
}

document.getElementsByClassName("command")[0].onmouseleave = function() {
    this.style.display = "none";
}

document.querySelector(".total").lastElementChild.onclick = function() {
    document.querySelector(".confirm-order").style.display = "block";
    document.querySelector(".pizza-menu").style.filter = "blur(10px)"
}

document.querySelector(".close-confirm").onclick = function() {
    document.querySelector(".confirm-order").style.display = "none";
    document.querySelector(".pizza-menu").style.filter = "blur(0px)"
}

document.getElementsByClassName("confirm-info")[0].onclick = function() {
    printWindow = window.open("","_blank","width = 500 , height = 500");
    printWindow.document.write (`
        <!DOCTYPE html>
        <html lang="en">
        <html>
        <head>
            <meta charset = "UTF-8"
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>ticket</title>
            <style>
                * {
                    box-sizing: border-box;
                    padding: 0;
                    margin: 0;
                    font-family: system-ui;
                }
                .ticket {
                    width: 450px;
                    background: #eeeeee80;
                    padding: 10px;
                    margin: 50px auto;
                    border-radius: 8px;
                }

                .ticket .ticket-head {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                .ticket .ticket-head img {
                    max-width: 100%;
                    width: 80px;
                }

                .ticket .ticket-head .title {
                    font-size: 25px;
                }

                .client-info {
                    text-align: center;
                    padding: 10px;
                    border-bottom: 1px solid #ccc;
                }

                .client-info p {
                    margin-bottom: 5px;
                    letter-spacing: .5px;
                }

                .client-info p > span {
                    font-weight: 500;
                }

                .order-details {
                    width: 100%;
                    padding: 10px;
                    margin-top: 10px;
                    border-collapse: collapse;
                    text-align: center;
                }

                .order-details td {
                    padding: 5px;
                    border: 1px solid #333;
                }

                .order-details thead td {
                    font-weight: 500;
                }

                .ticket > p {
                    padding: 10px 0;
                    letter-spacing: .5px;
                    font-size: 18px;
                    text-align: right;
                }

                .ticket > p .total {
                    font-weight: 500;
                }
                
                button {
                    display: block;
                    margin: auto;
                    padding: 5px 15px;
                    font-size: 16px;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                    background: #e0e0e0;
                    cursor: pointer;
                    outline: none;
                    user-select: none;
                }

                @media print {
                    button {
                        display: none;
                    }
                }
            </style>
        </head>
        <body>
            <div class="ticket">
                <div class="ticket-head">
                    <img src="static/images/logo.png" alt="logo">
                    <div class="title">Slice Haven</div>
                </div>
                <div class="client-info">
                    <p>Client: <span class="name"> ${document.querySelector(".confirm-order").children[1].value} </span></p>
                    <p>Phone: <span class="phone"> ${document.querySelector(".confirm-order").children[2].value} </span></p>
                    <p>Address: <span class="address"> ${document.querySelector(".confirm-order").children[3].value} </span></p>
                    <p>Date: <span class = "data"> ${getCurrentDate()} </span></p>
                </div>
                <table class="order-details">
                    <thead>
                        <tr>
                            <td>Product</td>
                            <td>PU</td>
                            <td>Quantity</td>
                            <td>Price</td>
                        </tr>
                    </thead>
                    <tbody>
    `);
    
    for (let i = 0 ; i < document.querySelectorAll(".order").length ; ++i) {
        printWindow.document.write(`
            <tr>
                <td>${document.querySelectorAll(".order")[i].children[0].textContent}</td>
                <td>${document.querySelectorAll(".order")[i].children[1].textContent}</td>
                <td>${document.querySelectorAll(".order")[i].children[2].textContent}</td>
                <td>${parseInt(document.querySelectorAll(".order")[i].children[1].textContent) * parseInt(document.querySelectorAll(".order")[i].children[2].textContent.slice(1))} MAD</td>
            </tr>
        `)
    }

    printWindow.document.write(`
                    </tbody>
                </table>
                <p>Total: <span class="total">${parseInt(document.querySelector(".total").firstElementChild.textContent.slice(7))}</span> MD</p>
                <button id = "printButton" >Print</button>
            </div>
        </body>
        </html>   
    `);

    printWindow.document.getElementById("printButton").addEventListener("click",async(ev) => {
        const clientName = printWindow.document.querySelector(".name").textContent
        const clientPhone = printWindow.document.querySelector(".phone").textContent
        const orderDate = printWindow.document.querySelector(".data").textContent
        const orderTotal = printWindow.document.querySelector(".total").textContent

        const response = await fetch('/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({clientName: clientName,clientPhone : clientPhone,orderDate: orderDate , orderTotal : orderTotal}),
        });
        const result = await response.json();
        if (result.success) {
            printWindow.document.close();
            printWindow.print();
        }
    })
}

document.querySelectorAll(".open-options").forEach(element => {
    element.onclick = _ => {
        element.style.display = "none";
        element.nextElementSibling.style.display = "block";
    }
})

document.querySelectorAll(".options").forEach(element => {
    element.onmouseleave = _ => {
        element.style.display = "none";
        element.previousElementSibling.style.display = "block";
    }
})

document.querySelectorAll(".delete-option").forEach(element => {
    element.addEventListener("click", async(ev) => {
        const productId = parseInt(ev.target.parentElement.firstElementChild.textContent.slice(5))
        const productIdType = ev.target.parentElement.firstElementChild.dataset.idtype;
        const response = await fetch('/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({id: productId,idType : productIdType}),
        });
        const result = await response.json();
        if (result.success) {
            ev.target.parentElement.parentElement.parentElement.remove()
        }
    })
})

document.querySelectorAll(".update-option").forEach(element => {
    element.onclick = _ => {
        element.parentElement.parentElement.nextElementSibling.style.display = "block";
    }
})

document.querySelectorAll(".close-update").forEach(element => {
    element.onclick = _ => {
        element.parentElement.style.display = "none";
    }
})

document.querySelectorAll(".confirm-updates").forEach(element => {
    element.addEventListener("click", async(ev) => {
        const productId = parseInt(ev.target.dataset.id)
        const productIdType = ev.target.dataset.idtype;
        const newProductName = ev.target.parentElement.firstElementChild.nextElementSibling.value;
        const newProductPrice = ev.target.parentElement.firstElementChild.nextElementSibling.nextElementSibling.value;

        const response = await fetch('/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({id: productId,idType : productIdType,productName: newProductName , productPrice : newProductPrice}),
        });
        const result = await response.json();
        if (result.success) {
            location.reload()
        }
    })
})