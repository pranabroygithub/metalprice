export async function load({ fetch , url }) {
    //console.log("is time_period parameter defined: ", url.searchParams.get('timeperiod'))
    let priceOffset = 0;
    const timeperiod = url.searchParams.get('timeperiod') || '3Y';
    const currency_type = url.searchParams.get('currency_type') || 'inr';
    let url_str = `http://127.0.0.1:8000/getgoldpricehistory?timeperiod=${timeperiod}&currency_type=${currency_type}`
    const response = await fetch(url_str);

    if (!response.ok) {
        throw new Error('Failed to fetch gold price');
    }

    if(currency_type == 'inr') {priceOffset=10000;}
    if(currency_type == 'usd') {priceOffset=100;}
    const gold_price = await response.json();
    return {
        gold_price: gold_price,
        priceOffset: priceOffset
    };
}
