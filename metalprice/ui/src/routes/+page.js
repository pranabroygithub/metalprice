export async function load({ fetch , url }) {
    //console.log("is time_period parameter defined: ", url.searchParams.get('timeperiod'))
    let priceOffset = 0;
    let currency_type = 'inr';
    let timeperiod = '1Y';
    let metal_type = 'XAU';
    timeperiod = url.searchParams.get('timeperiod') || timeperiod;
    currency_type = url.searchParams.get('currency_type') || currency_type;
    metal_type = url.searchParams.get('metal_type') || metal_type;
    let url_str = `http://127.0.0.1:8000/getmetalpricehistory?timeperiod=${timeperiod}&currency_type=${currency_type}&metal_type=${metal_type}`
    console.log(url_str)
    const response = await fetch(url_str);

    if (!response.ok) {
        throw new Error('Failed to fetch gold price');
    }

    if(metal_type == 'XAG' && currency_type == 'inr') {priceOffset=1000;}
    if(metal_type == 'XAG' && currency_type == 'usd') {priceOffset=10;}
    if(metal_type == 'XAU' && currency_type == 'inr') {priceOffset=10000;}
    if(metal_type == 'XAU' && currency_type == 'usd') {priceOffset=500;}
    const metal_price = await response.json();
    return {
        metal_price: metal_price,
        priceOffset: priceOffset,
        currency_type: currency_type,
        timeperiod: timeperiod,
        metal_type: metal_type
    };
}
