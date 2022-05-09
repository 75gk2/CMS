<!--<script>-->
<!--    // links.push({})-->
<!--</script>-->

<!--<div>Formularz</div>-->


<!--<div>Tabelka aktualnych-->
<!--    {#each links as link}-->
<!--        <div>text = {link.text} href = {link.href} <button>Edytuj</button></div>-->
<!--    {/each}-->
<!--</div>-->
<script>
    export let headerData;
    console.log(headerData)
    let links = [];
    import {writable} from 'svelte/store';

    const user = writable({
        name: "",
    })

    function mySubmit(){
        links.push({name:$user.name})
        $user.name = ""
        console.log(links)
    }
</script>

<h1>Form</h1>
<form on:submit|preventDefault={mySubmit}>
    <label>Name</label>
        <input type="text" bind:value={$user.name}/>
    <input type="submit">
</form>
<p>
    {JSON.stringify($user, 0, 2)}
</p>

