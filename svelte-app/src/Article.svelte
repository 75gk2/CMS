<script>
    console.log("THIS")
    import {Article, Net} from "./net";

    export let link
    let data = Article.getArticle(link)
    export let loginData
    let newCom = ""

    function addCom() {
        let com = {
            nick: $loginData.login,
            content: newCom,
        }
        newCom = ""
        data.then(d => {
            d.comments.push(com)
            let res = Article.updateArticle(d, link)
            res.then(() => data = Article.getArticle(link))
        })
    }

    let show = false

    function showPhoto() {
        show = true
    }
</script>

{#await data}
    Loading...
{:then data}
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
            <div class="flex flex-col text-center w-full mb-20">
                <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">{data.title}</h1>
                <p class="lg:w-2/3 mx-auto leading-relaxed text-base">{data.description}</p>
            </div>
            <div class="flex flex-wrap -m-4">

                {#each data.images as img}

                    <div class="lg:w-1/3 sm:w-1/2 p-4">
                        <div class="flex relative">

                            {#await Net.fetchPhoto(img.src)}
                                Loading photo...
                            {:then photo}
                                <img
                                        src="{photo}"
                                        class="absolute inset-0 w-full h-full object-cover object-center"
                                        alt="PHOTO SRC={photo}"
                                />
                                <div class="h-64 px-8 py-10 relative z-10 w-full border-4 border-gray-200 bg-white opacity-0 hover:opacity-75"
                                     on:click={(e)=>{show = img.src}}>
                                    <h1 class=" title-font text-lg font-medium text-gray-900 mb-3">{img.title}</h1>
                                    <p class="leading-relaxed ">{img.description}</p>
                                </div>

                                {#if show === img.src}
                                    <div class="fixed z-50 top-0 left-0 w-full h-full bg-gray-50 p-50" on:click={()=>{show = ""}}>
                                        <img
                                                src="{photo}"
                                                class="inset-0 object-cover object-center"
                                                alt="PHOTO SRC={photo}"
                                        />
                                    </div>
                                {/if}
                            {/await}
                        </div>
                    </div>
                {/each}
            </div>
        </div>
    </section>

    {#if $loginData.isLogged}
        {#if data.status !== -1}
            <div class="border border-gray-500 m-10">
                <h1 class="text-3xl font-medium title-font text-gray-900 text-right absolute right-1/3 mt-20">
                    Comments:</h1>
                <div class="mt-10">
                    <label class="mx-10">Add comment
                        <input id="copy" type="text"
                               bind:value={newCom}
                               class="mx-10 my-5 w-1/3 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"/>
                    </label>
                    <button on:click={addCom}
                            class="mx-5  px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">
                        Submit
                    </button>
                </div>
                <section class="text-gray-600 body-font">
                    <div class="container px-5 py-24 mx-auto">
                        <div class="flex flex-wrap -m-4">
                            {#each data.comments as com}
                                <div class="p-4 md:w-1/2 w-full">
                                    <div class="h-full bg-gray-100 p-8 rounded">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                             class="block w-5 h-5 text-gray-400 mb-4" viewBox="0 0 975.036 975.036">
                                            <path d="M925.036 57.197h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.399 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l36 76c11.6 24.399 40.3 35.1 65.1 24.399 66.2-28.6 122.101-64.8 167.7-108.8 55.601-53.7 93.7-114.3 114.3-181.9 20.601-67.6 30.9-159.8 30.9-276.8v-239c0-27.599-22.401-50-50-50zM106.036 913.497c65.4-28.5 121-64.699 166.9-108.6 56.1-53.7 94.4-114.1 115-181.2 20.6-67.1 30.899-159.6 30.899-277.5v-239c0-27.6-22.399-50-50-50h-304c-27.6 0-50 22.4-50 50v304c0 27.601 22.4 50 50 50h145.5c-1.9 79.601-20.4 143.3-55.4 191.2-27.6 37.8-69.4 69.1-125.3 93.8-25.7 11.3-36.8 41.7-24.8 67.101l35.9 75.8c11.601 24.399 40.501 35.2 65.301 24.399z"></path>
                                        </svg>
                                        <p class="leading-relaxed mb-6 break-all">{com.content}</p>
                                        <a class="inline-flex items-center">
                                            <span class="title-font font-medium pl-4 text-gray-900">{com.nick}</span>
                                        </a>
                                    </div>
                                </div>
                            {/each}
                        </div>
                    </div>
                </section>
            </div>
        {/if}
    {/if}
{/await}