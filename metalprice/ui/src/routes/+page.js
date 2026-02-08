export async function load({ fetch }) {
  const response = await fetch('http://127.0.0.1:8000/getgoldpricehistoryininr');

  if (!response.ok) {
    throw new Error('Failed to fetch gold price');
  }

  const gold_price = await response.json();

  return {
    gold_price
  };
}
