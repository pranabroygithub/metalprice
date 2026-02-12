<script>
	// original: https://observablehq.com/@d3/line-chart/2
	// svelte version: Sebastian Lammers https://vis.social/@seblammers

	import LineChart from './LineChart.svelte';
    let { metal_price, priceOffset} = $props();	
    //console.log("App.svelte gold price = ", metal_price)

</script>

<LineChart metal_price={metal_price} priceOffset={priceOffset} />
