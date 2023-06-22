function nameWallet(evt, text){
    const textBlock = document.getElementsByClassName("nameWallet")[0];
    const activeWalet = document.getElementsByClassName("activeWallet")[0];
    const min = document.getElementsByClassName("minMoney")[0];
    const max = document.getElementsByClassName("maxMoney")[0];
    const btnValue = document.getElementsByClassName("btnValue");
    const input = document.getElementsByClassName("inputMoneyM")[0];

    activeWalet.classList.remove("activeWallet");
    evt.currentTarget.classList.add("activeWallet");

    switch(text){
        case "Binance Pay":
            min.innerHTML = "250₽";
            max.innerHTML = "69 000 000₽";
            input.placeholder = "400";
            input.value = "400";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "400");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "700");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "1 000");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "2 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "5 000");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "10 000");
                }
            }

            break;
        case "LiteCoin":
            min.innerHTML = "200₽";
            max.innerHTML = "69 000 000₽";
            input.placeholder = "200";
            input.value = "200";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "200");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "1 000");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "2 000");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "7 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "5 000");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "10 000");
                }
            }

            break;
        case "BitCoin":
            min.innerHTML = "600₽";
            max.innerHTML = "69 000 000₽";
            input.placeholder = "1 000";
            input.value = "1 000";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "1 000");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "5 000");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "7 000");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "10 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "15 000");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "20 000");
                }
            }

            break;
        case "Ethereum":
            min.innerHTML = "1 500₽";
            max.innerHTML = "69 000 000₽";
            input.placeholder = "1 500";
            input.value = "1 500";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "1 500");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "7 000");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "10 000");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "15 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "20 000");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "25 000");
                }
            }

            break;
        case "DogeCoin":
            min.innerHTML = "200₽";
            max.innerHTML = "69 000 000₽";
            input.placeholder = "200";
            input.value = "200";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "200");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "1 000");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "2 000");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "5 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "7 000");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "10 000");
                }
            }

            break;
        default: 
            min.innerHTML = "100₽";
            max.innerHTML = "300 000₽";
            input.placeholder = "100";
            input.value = "100";
            for(let i = 0; i < btnValue.length; i++ ){
                if(i == 0){
                    btnValueChange(btnValue[i], "100");
                }else if(i === 1){
                    btnValueChange(btnValue[i], "200");
                }else if(i === 2){
                    btnValueChange(btnValue[i], "500");
                }else if(i === 3){
                    btnValueChange(btnValue[i], "1 000");
                }else if(i === 4){
                    btnValueChange(btnValue[i], "1 500");
                }else if(i === 5){
                    btnValueChange(btnValue[i], "2 000");
                }
            }
            break;
    }
    textBlock.innerHTML = text;
}

function btnValueChange(evt, number){
    evt.innerHTML = number, 
    evt.value = number;
}

function addMoneyInInput(evt){
    const text = evt.currentTarget.value;
    const input = document.getElementsByClassName("inputMoneyM")[0];
    const activeMoney = document.getElementsByClassName("activeMoney")[0];

    if(activeMoney !== undefined){
        activeMoney.classList.remove("activeMoney");
    }
    evt.currentTarget.classList.add("activeMoney");
    
    input.value = text;
}

function inputFunction(evt){
    const activeMoney = document.getElementsByClassName("activeMoney")[0];
    if(activeMoney !== undefined){
        activeMoney.classList.remove("activeMoney");
    }
   
}

function copy() {
    const value = document.getElementsByClassName("upiInput")[0].value;
    navigator.clipboard.writeText(value);
}