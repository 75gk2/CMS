<script>
    import Router from 'svelte-spa-router'
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import * as data from './data.json'
    console.log(data)
</script>

<main>
<!--    <Website data={data}/>-->
    <MainForm data={data}></MainForm>
</main>

<!--<Router routes = {{-->
<!--    "/": MainForm-->
<!--}}/>-->