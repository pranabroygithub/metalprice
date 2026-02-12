<script>
	import PlaygroundLayout from '$lib/PlaygroundLayout.svelte';
    import App from '$lib/playground/App.svelte';
	let { data } = $props();
	//console.log("page.svelte metal_price" , data.metal_price)
	
</script>
<PlaygroundLayout currency_type={data.currency_type} timeperiod={data.timeperiod} metal_type={data.metal_type}>
    <App metal_price={data.metal_price} priceOffset={data.priceOffset}/>
</PlaygroundLayout>
