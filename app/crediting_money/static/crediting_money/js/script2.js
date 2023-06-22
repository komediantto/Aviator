function nameWallet2(evt, text){
    const textBlock = document.getElementsByClassName("nameWallet")[0];
    const activeWalet = document.getElementsByClassName("activeWallet")[0];
    const min = document.getElementsByClassName("minMoney")[0];
    const max = document.getElementsByClassName("maxMoney")[0];
    const input = document.getElementsByClassName("inputMoneyM")[0];
    const inputNumber = document.getElementsByClassName("divInputNumber")[0];
    const inputName = document.getElementsByClassName("divInputName")[0];
    const inputLastName = document.getElementsByClassName("divInputLastName")[0];


    activeWalet.classList.remove("activeWallet");
    evt.currentTarget.classList.add("activeWallet");

    switch(text){
        case "ecoPayz":
            min.innerHTML = "300₽";
            max.innerHTML = "100 000₽";
            input.placeholder = "300";
            break;
        case "Binance Pay":
            min.innerHTML = "1 000₽";
            max.innerHTML = "800 000₽";
            input.placeholder = "1 000";
            break;
        case "BitCoin":
            min.innerHTML = "1 000₽";
            max.innerHTML = "800 000₽";
            input.placeholder = "1 000";

            break;
        case "Ethereum":
            min.innerHTML = "1 000₽";
            max.innerHTML = "800 000₽";
            input.placeholder = "1 000";

            break;
        default: 
            min.innerHTML = "500₽";
            max.innerHTML = "50 000₽";
            input.placeholder = "500";
            inputNumber.style.display = "flex";
            inputName.style.display = "flex";
            inputLastName.style.display = "flex";

            break;
    }
    textBlock.innerHTML = text;
}
