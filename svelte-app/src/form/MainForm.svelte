<script>
    import NewsForm from "./NewsForm.svelte";

    const data_json = (async () => {
        const response = await fetch('http://127.0.0.1:5000/data')
        return await response.json()
    })()

    data_json.then((d)=>FormNet.json = d)

    import HeaderForm from "./HeaderForm.svelte";
    import SliderForm from "./SliderForm.svelte";
    import {FormNet} from "../net";
    import FooterForm from "./FooterForm.svelte";

</script>
{#await data_json}
    Loading...
{:then data}
    <button on:load={()=>{FormNet.json = data}} on:click={()=>FormNet.updateData()}
            class="fixed top-2 m-4 px-6 py-2.5 bg-yellow-400 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-yellow-500 hover:shadow-lg focus:bg-yellow-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-yellow-800 active:shadow-lg transition duration-150 ease-in-out">
        UPDATE
    </button>
    <div class = "mt-20">
    <HeaderForm formNet={FormNet} headerData = {data.header}></HeaderForm>
    <SliderForm formNet={FormNet} sliderData={data.content.slider}></SliderForm>
    <NewsForm formNet={FormNet} newsData={data.content.news}></NewsForm>
    <FooterForm formNet={FormNet} footerData = {data.footer}></FooterForm>
    </div>
{/await}