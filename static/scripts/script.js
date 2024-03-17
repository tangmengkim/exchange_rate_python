function amount_convertor(amount,to_bid,to_ask){
    var toBid_selected = to_bid.options[to_bid.selectedIndex];
    var toAsk_selected = to_ask.options[to_ask.selectedIndex];
    var toBidCurrency = toBid_selected.textContent;
    var toAskCurrency = toAsk_selected.textContent;
    var toBidSymbol = symbolCurrency(toBidCurrency);
    var toAskSymbol = symbolCurrency(toAskCurrency);
    amount = parseFloat(amount);
    
    // To Split dataValue as array ###&#### -> [###, ####]
    to_bid = toBid_selected.value.split("&");
    to_ask = toAsk_selected.value.split("&");

    // To check selection
    if (to_ask != "" && to_bid != "" && amount) {
    let ask,bid;
    // To check if 2selector is the same value
    if (to_bid[0] == to_ask[0]){
        ask = parseFloat(to_ask[0]);
        bid = parseFloat(to_bid[0]);
    }else{
        ask = parseFloat(to_ask[1]);
        bid = parseFloat(to_bid[0]);
    }
    // calculator
    let converted = amount*((bid)/(ask));
    // format float by setpoint (0.00)
    converted_amount = converted.toFixed(2);
    amount = amount.toFixed(2);
    // set converted amount to string
    converted_amount_text = `${amount} ${toBidSymbol} = ${converted_amount}  ${toAskSymbol} `;

    return converted_amount_text;
    } 
    else return "";
    }

function swap_currency(){
    var to_ask = document.getElementById("to_ask");
    var to_bid = document.getElementById("to_bid");
    var swap = to_ask.value;
    to_ask = to_bid.value;
    to_bid = swap ;
    document.getElementById("to_ask").value = to_ask;
    document.getElementById("to_bid").value = to_bid;
    document.getElementById("input-amount").value = "";
    document.getElementById("output-amount").value = "";
}

function symbolCurrency(currency){
    const symbol={
        "KHR" : "៛",
        "USD" : "$",
        "THB" : "฿",
        "EUR" : "€",
        "AUD" : "$",
        "VND" : "₫",
        "CAD" : "$",
        "LAK" : "₭",
        "JPY" : "¥",
        "GBP" : "£",
        };
    return symbol[currency];
    }