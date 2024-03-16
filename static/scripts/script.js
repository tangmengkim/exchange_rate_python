function amount_convertor(amount,to_bid,to_ask){
    to_bid = to_bid.split("&");
    to_ask = to_ask.split("&");
    let ask,bid;
    if (to_bid[0] == to_ask[0]){
        ask = parseFloat(to_ask[0]);
        bid = parseFloat(to_bid[0]);
    }else{
        ask = parseFloat(to_ask[1]);
        bid = parseFloat(to_bid[0]);
    }
    console.log(ask);
    let converted = amount*((bid)/(ask));
    // format float by setpoint (0.00)
    converted_amount = converted.toFixed(2)
    return converted_amount
}

function swap_currency(){
    alert("test");
    return false;
}
