const searchField = document.querySelector("#searchField");

const appTable = document.querySelector(".app-table");
const tableOutput = document.querySelector(".table_output");
const tableContainer = document.querySelector(".table-container");
const tableBody = document.querySelector(".table-body");
let dataSearch = [];
tableOutput.style.display ="none"


searchField.addEventListener('keyup', (e)=>{
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0){
        tableContainer.style.display = "none";
        tableBody.innerHTML = '';
        fetch("/search_customer", {
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data)=> {
            console.log("data", data);
            dataSearch = data;
            appTable.style.display = "none";
            tableOutput.style.display = "block";

            if (data.length ===0){
                tableOutput.innerHTML +=`không có dữ liệu <a href="http://127.0.0.1:8000/add">Thêm</a>`;
            }else{
                data.forEach((item) => {
                    tableBody.innerHTML +=`
                    <tr onclick="myFunction(${item.id})" style="font-size: 10px;">
                        <td style="display: none;">${item.id}</td>
                        <td id="name">${item.name}</td>
                        <td id="mail">${item.email}</td>
                        <td>${item.phone}</td>
                    </tr
                    `;
                
                })
            }
        });

    }else{
        tableOutput.style.display="none";
        appTable.style.display = "block";
        tableContainer.style.display = "block";
    }

});

function myFunction(id) {
    let selectData = dataSearch.find(item => item.id == id);
    document.getElementById("email").value = selectData.email;
    document.getElementById("customer-name").value = selectData.name;
    
  }