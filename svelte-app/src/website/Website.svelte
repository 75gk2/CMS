<script>
    import Header from './Header.svelte';
    import Slider from "./Slider.svelte";
    import News from "./News.svelte";
    import Footer from "./Footer.svelte";
    export let data;
</script>


<Header headerData={data.header}/>
<Slider sliderData={data.content.slider}></Slider>
<News newsData={data.content.news}></News>
<Footer footerData={data.footer}></Footer>
