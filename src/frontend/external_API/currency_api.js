document
  .querySelector('#currencyChange')
  .addEventListener('change', changeCurrency);

async function changeCurrency() { 
    const currency = document
    .querySelector('#currencyChange').value
    let converter = 1
    if(currency == 'eur'){
    const response = await fetch("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json").then((rsp) => rsp.json())
    .then((obj) =>{ converter = (obj.usd[currency])})
    }
    
    (document.querySelectorAll("#montoShow")).forEach(element => {
        (element.textContent= (element.getAttribute("value")*converter).toFixed(2))
    });
}