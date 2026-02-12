<script>
	// original: https://observablehq.com/@d3/line-chart/2
	// svelte version: Sebastian Lammers https://vis.social/@seblammers

	import LineChart from './LineChart.svelte';
    let { gold_price, priceOffset} = $props();	
    //console.log("App.svelte gold price = ", gold_price)

</script>

<LineChart gold_price={gold_price} priceOffset={priceOffset} />
