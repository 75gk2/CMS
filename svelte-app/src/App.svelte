<script>
	export let name;

	var theme;

	function sendForm() {
		alert("sus");
	}
</script>

<main>
	<!--#2
	<h1>Hello {name}!</h1>
	<p>
		Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
		how to build Svelte apps.
	</p>-->

	<div>
		<h2>Menu layout:</h2>
		<form>
			<span>horizontal:</span>
			<input type="radio" name="menu" value="horizontal" checked />
			<br />
			<span>vertical:</span>
			<input type="radio" name="menu" value="vertical" />
		</form>
	</div>
	<div>
		<h2>Elements order:</h2>
		<form>
			<select name="orderSelect" id="orderSelect">
				<option value="slider-news" selected
					>menu-slider-news-footer</option
				>
				<option value="news-slider">menu-news-slider-footer</option>
			</select>
		</form>
	</div>
	<div>
		<h2>Slider speed:</h2>
		<form>
			<span>1 second</span>
			<input
				id="sliderSpeedInput"
				type="range"
				min="1000"
				max="5000"
				value="3000"
				step="100"
			/>
			<span>5 seconds</span>
		</form>
	</div>
	<div>
		<h2>Font family:</h2>
		<form>
			<select name="themeSelect" id="themeSelect">
				<option value="Arial" selected>Arial</option>
				<option value="Monaco">Monaco</option>
				<option value="Times_New_Roman">Times New Roman</option>
			</select>
		</form>
	</div>
	<div>
		<h2>Theme:</h2>
		<form>
			<select name="themeSelect" id="themeSelect" bind:value={theme}>
				<option value="default" selected>default</option>
				<option value="dark">dark</option>
				<option value="custom">custom</option>
			</select>
		</form>
		{#if theme === "custom"}
			<span>color: </span><input type="color" id="customColorInput" /><br
			/>
			<span>background-color: </span><input
				type="color"
				id="customBackgroundColorInput"
			/><br />
			<span>border-color: </span><input
				type="color"
				id="customBorderColorInput"
			/>
		{/if}
	</div>

	<a on:click={sendForm}>Save</a>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	a {
		margin: 20px;
		cursor: pointer;
	}
</style>
