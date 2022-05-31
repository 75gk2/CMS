<script>
    import {Article} from "./net";
    import {writable} from "svelte/store";

    let text
    let validLinks = writable({
        validLinks :[]
    })
    const find = async () => {
        const response = await fetch('http://127.0.0.1:5000/data')
        const json = await response.json()
        const tab = []

        function chkLink(l) {
            if (!tab.includes(l.href) && l.href !== "")
                tab.push(l.href)
        }

        json.header.menu.links.forEach(e => chkLink(e))
        json.content.news.forEach(e => chkLink(e))
        json.footer.links.forEach(e => chkLink(e))
        $validLinks.validLinks = await Promise.all(tab.filter(async (e)=>{
            console.log(e)
            let res = await Article.getArticle(e)
            if ((res.title).includes(text)){
                console.log(res, text)
                return e
            }
            if ((res.description).includes(text)) {
                return  e
            }
        }))
    }
</script>


<div class="mt-10">
    <label class="mx-10">Search in articles
        <input id="copy" type="text"
               bind:value={text}
               class="mx-10 my-5 w-1/3 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"/>
    </label>
    <button on:click={find}
            class="mx-5  px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">
        Submit
    </button>
</div>
<ul>
    {#each $validLinks.validLinks as thisLink}
        <li>
            <a href="{thisLink}">{thisLink}</a>
        </li>
    {/each}
</ul>