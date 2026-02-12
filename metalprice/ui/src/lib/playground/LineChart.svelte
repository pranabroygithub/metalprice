<script>
    import * as d3 from "d3";
	// Import axes-components.
	import AxisY from './AxisY.svelte';
	import AxisX from './AxisX.svelte';

    // Receive plot data as prop.
    let { gold_price = [], priceOffset = 0 } = $props();	

    //console.log("Line chart gold_price = " , gold_price)

  const width = 1366;
  const height = 500;
  
	const margin = { 
		top: 10,
		right: 20,
		bottom: 20,
		left: 80	
	};
  // Declare the x (horizontal position) scale.
  let xScale = $derived(d3.scaleUtc()
      .domain(d3.extent(gold_price, d => new Date(d.day)))
      .range([margin.left, width - margin.right]));

  // Declare the y (vertical position) scale.
 
  let yScale = $derived(d3.scaleLinear()
      .domain([d3.min(gold_price, d => d.max_price - priceOffset), d3.max(gold_price, d => d.max_price + priceOffset)])
      .rangeRound([height - margin.bottom, margin.top]));

  // Declare the line generator.
  let line = $derived(d3.line()
      .x(d => xScale(new Date(d.day)))
      .y(d => yScale(d.max_price)));
</script>

<svg
  {width}
  {height}
  viewBox="0 0 {width} {height}"
  style:max-width="100%"
  style:height="auto"
>
	<!-- Add the y-axis -->
	<AxisY yScale={yScale} width={width} margin={margin} />

	<!-- Add the x-axis -->
	<AxisX xScale={xScale} height={height} margin={margin} />

	<!-- Add a path for the line. -->
	<g class="data">
			<path 
				fill=none
				stroke="yellow"
				d={line(gold_price)}/>
	</g>
</svg>
