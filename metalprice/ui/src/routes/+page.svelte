<script>
	import PlaygroundLayout from '$lib/PlaygroundLayout.svelte';
    import App from '$lib/playground/App.svelte';
	let { data } = $props();
	//console.log("page.svelte gold_price" , data.gold_price)
	
</script>
<PlaygroundLayout>
    <App gold_price={data.gold_price} priceOffset={data.priceOffset}/>
</PlaygroundLayout>
