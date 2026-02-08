<script>
	// Receive y-scale, width and margins as props.
	let {yScale, width, margin} = $props();

	// Determine ticks based on y-scale.
	// Try changing this number to haver e.g. fewer ticks.
    let yTicks = $derived(yScale.ticks(10));
</script>

<g class="y-axis" transform="translate({margin.left}, 0)">

	<!-- 
		Loop through the y-ticks defined in the script tag 
		and define a tick with it's label respectively.
	-->
	{#each yTicks as tick, index}
		<g class='tick' transform="translate(0, {yScale(tick)})">

			<!-- Y-Axis Ticks -->
			<line x1={0} x2={width} y1={0} y2={0} stroke="hsla(212, 10%, 53%, 0.3)" /> 

			<!-- Y-Axis Tick Labels -->
			<text 
				x={-5} 
				y={0} 
				fill="currentColor"
				dominant-baseline="middle" 
				text-anchor="end">
				{tick}
			</text>
		</g>
	{/each}
</g>
