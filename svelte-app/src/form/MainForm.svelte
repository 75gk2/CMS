<script>
    import NewsForm from "./NewsForm.svelte";

    export let data;
    import HeaderForm from "./HeaderForm.svelte";
    import SliderForm from "./SliderForm.svelte";
</script>


<!--<HeaderForm headerData = {data.header}></HeaderForm>-->
<SliderForm sliderData = {data.content.slider}></SliderForm>
<NewsForm newsData = {data.content.news}></NewsForm>
