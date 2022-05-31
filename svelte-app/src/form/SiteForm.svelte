<script>
    import {writable} from "svelte/store";
    import "tw-elements";
    import {Article, Net} from "../net";


    const links = (async () => {
        const response = await fetch('http://127.0.0.1:5000/data')
        const json = await response.json()
        console.log(json)
        const tab = []
        function chkLink(l) {
            if (!tab.includes(l.href) && l.href !== "")
                tab.push(l.href)
        }
        json.header.menu.links.forEach(e => chkLink(e))
        json.content.news.forEach(e => chkLink(e))
        json.footer.links.forEach(e => chkLink(e))
        $href.href = tab[0]
        sync()
        console.log(tab)
        return tab
    })()

    let href = writable({
        href: ""
    })
    let commentsHolder = []
    let slides = []
    console.log(slides.length)

    function swapUp(i) {
        if (i !== 0) {
            const tmp = slides[i - 1];
            slides[i - 1] = slides[i];
            slides[i] = tmp;
        }
    }

    function swapDown(i) {
        if (i !== slides.length - 1) {
            const tmp = slides[i + 1];
            slides[i + 1] = slides[i];
            slides[i] = tmp;
        }
    }

    const newsFormValues = writable({
        title: "",
        description: "",
        src: "",
        position: slides.length + 1,
    });

    const siteFormValues = writable({
        title: "",
        description: ""
    });

    function newsFormSubmit() {
        const obj = {
            title: $newsFormValues.title,
            description: $newsFormValues.description,
            src: $newsFormValues.src.replace("C:\\fakepath\\", ''),
        };
        let position = $newsFormValues.position;

        if (formStatus !== -1) del(formStatus);

        console.log(file)

        if (file != null) Net.sendPhoto(obj.src, file)


        file = null

        slides.splice(position - 1, 0, obj);
        slides = slides;

        console.log(slides, slides.length + 1);
        $newsFormValues.title = "";
        $newsFormValues.description = "";
        $newsFormValues.src = "";
        $newsFormValues.position = slides.length + 1;
    }

    let formStatus = -1; //-1: adding new news; <=0 : editing selected index

    function edit(i) {
        const obj = slides[i];
        formStatus = i;
        $newsFormValues.title = obj.title;
        $newsFormValues.description = obj.description;
        $newsFormValues.src = obj.src;
        $newsFormValues.position = i + 1;
    }

    function del() {
        slides.splice(formStatus, 1);
        slides = slides;
        cancel();
    }

    function cancel() {
        $newsFormValues.title = "";
        $newsFormValues.description = "";
        $newsFormValues.src = "";
        $newsFormValues.position = slides.length + 1;
        formStatus = -1;
    }

    let file;

    function onFileSelected(e) {
        file = e.target.files[0];
    }

    function send() {
        const obj = {
            title: $siteFormValues.title,
            description: $siteFormValues.description,
            images: slides,
            comments:""
        }
        console.log(obj)
        Article.updateArticle(obj, $href.href)
    }
    function sync(){
        console.log($href.href)
        let res = Article.getArticle($href.href)
        res.then((data)=>{
            $siteFormValues.title = data.title
            $siteFormValues.description = data.description
            slides = data.images
            commentsHolder = data.comments
        })
    }
</script>
{#await links}
    Loading...
{:then links}
    <div class="flex justify-center mt-20">
        <div class="mb-3 xl:w-96">
            <select bind:value={$href.href} on:change={sync} on:load={sync}
                    class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                    aria-label="Default select example">
                {#each links as link,i}
                        <option>{link}</option>
                {/each}
            </select>
        </div>
    </div>
{/await}

<div class="border border-gray-300 m-10 px-10 pb-10">
    <h1 class="p-5">Form</h1>
    <div class="m-4">
        <label>title<input
                type="text"
                bind:value={$siteFormValues.title}
                class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
        /></label>
    </div>
    <div class="m-4">
        <label>description<textarea
                type="text"
                bind:value={$siteFormValues.description}
                class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"></textarea></label>
    </div>
    <br><br>
    <h1 class="p-5">Gallery</h1>
    <div class="flex flex-row">

        <form
                on:submit|preventDefault={() => newsFormSubmit()}
                class="w-1/3  border border-gray-300"
        >
            <h3 class="m-4">
                {#if formStatus === -1}
                    Adding new element:
                {:else}
                    Editing element: (title:{slides[formStatus].title}
                {/if}
            </h3>
            <div class="m-4">
                <label>title<input
                        type="text"
                        bind:value={$newsFormValues.title}
                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                /></label>
            </div>
            <div class="m-4">
                <label>description<textarea
                        type="text"
                        bind:value={$newsFormValues.description}
                        class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"></textarea></label>
            </div>
            <div class="m-4">
                <label>src
                    <input type="file" accept=".jpg, .jpeg, .png"
                           on:change={(e)=>onFileSelected(e)}
                           bind:value={$newsFormValues.src}
                           class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                           id="formFile"></label>
            </div>
            <div class="m-4">
                <label>position<input
                        type="number"
                        min="1"
                        max={formStatus === -1 ? slides.length + 1 : slides.length}
                        bind:value={$newsFormValues.position}
                        class=" form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                /></label>
            </div>
            <div class="flex flex-row">
                <button type="submit"
                        class="m-4 px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">

                    Submit
                </button>
                {#if formStatus !== -1}
                    <button on:click={del} type="button"
                            class="m-4 px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out">
                        Delete
                    </button>
                    <button on:click={cancel} type="button"
                            class="m-4 px-6 py-2.5 bg-yellow-400 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-yellow-500 hover:shadow-lg focus:bg-yellow-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-yellow-800 active:shadow-lg transition duration-150 ease-in-out">
                        Cancel
                    </button>
                {/if}
            </div>
        </form>

        <table class="ml-4 content-list w-2/3">
            <tr>
                <th class="border border-slate-300">title</th>
                <th class="border border-slate-300">description</th>
                <th class="border border-slate-300">file</th>
                <th class="border border-slate-300">edit</th>
            </tr>
            {#each slides as oneSlide, i}
                <tr>
                    <td
                            class="border border-slate-300 text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                    >{oneSlide.title}</td
                    >
                    <td
                            class="border border-slate-300 text-sm text-gray-900 font-light px-6 py-4"
                    >{oneSlide.description}</td
                    >
                    <td
                            class="border border-slate-300 text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                    >{oneSlide.src}</td
                    >
                    <td
                            class="border border-slate-300 text-sm text-gray-900 font-light px-3 py-1 whitespace-nowrap"
                    >
                        <div class="flex flex-row justify-around">
                            <button
                                    on:click={() => edit(i)}
                                    class="edit px-4 uppercase">edit
                            </button
                            >
                            <div class="flex flex-col">
                                <button class="arrow" on:click={() => swapUp(i)}>
                                    <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            class="h-6 w-6"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                    >
                                        <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M5 15l7-7 7 7"
                                        />
                                    </svg>
                                </button>
                                <button class="arrow" on:click={() => swapDown(i)}>
                                    <svg
                                            xmlns="http://www.w3.org/2000/svg"
                                            class="h-6 w-6"
                                            fill="none"
                                            viewBox="0 0 24 24"
                                            stroke="currentColor"
                                            stroke-width="2"
                                    >
                                        <path
                                                stroke-linecap="round"
                                                stroke-linejoin="round"
                                                d="M19 9l-7 7-7-7"
                                        />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </td>
                </tr>
            {/each}

            {#each slides.length>3?Array(0):Array(3 - slides.length) as _ }<div>&nbsp</div>{/each}
        </table>
    </div>
    <button on:click={send} type="button"
            class="m-4 px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out">
        UPDATE
    </button>

</div>

<style>
    .edit:hover,
    .arrow:hover svg {
        color: #00e9ff;
    }

    .content-list tr:nth-child(2) .arrow:first-child svg {
        opacity: 0.3;
    }

    .content-list tr:last-child .arrow:last-child svg {
        opacity: 0.3;
    }

    .content-list tr:nth-child(2) .arrow:first-child:hover svg {
        opacity: 0.3;
        color: black;
    }

    .content-list tr:last-child .arrow:last-child:hover svg {
        opacity: 0.3;
        color: black;
    }
</style>