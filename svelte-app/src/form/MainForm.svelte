<script>
    export let data;
    import HeaderForm from "./HeaderForm.svelte";
    import SliderForm from "./SliderForm.svelte";
</script>


<HeaderForm headerData = {data.header}></HeaderForm>
<SliderForm></SliderForm>