export async function load({ fetch , url }) {
    //console.log("is time_period parameter defined: ", url.searchParams.get('timeperiod'))
    const timeperiod = url.searchParams.get('timeperiod') || '3Y';
    let url_str = `http://127.0.0.1:8000/getgoldpricehistoryininr?timeperiod=${timeperiod}`
    //console.log(url_str)
    const response = await fetch(url_str);

    if (!response.ok) {
        throw new Error('Failed to fetch gold price');
    }

    const gold_price = await response.json();

    return {
        gold_price
    };
}
