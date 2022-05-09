<script>
	import Header from './Header.svelte';
	import * as data from './data.json'
	import Slider from "./Slider.svelte";
	import News from "./News.svelte";
	import Footer from "./Footer.svelte";

</script>

<main>
	<Header headerData = {data.header}/>
	<Slider sliderData = {data.content.slider}></Slider>
	<News newsData = {data.content.news}></News>
	<Footer footerData = {data.footer}>xdxd</Footer>
</main>
