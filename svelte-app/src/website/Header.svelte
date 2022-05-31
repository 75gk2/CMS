<script>
    export let headerData;
    import {Net} from "../net";

    console.log(headerData.menu.links)
</script>
{#if headerData.menu.type == "poziome"}
    <header class="text-gray-600 body-font">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
            <div class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
                {#if headerData["logo"] !== undefined}
                    {#await Net.fetchPhoto(headerData.logo.src)}
                        Loading photo...
                    {:then photo}
                        <img style="width:{headerData.logo.width}; height:{headerData.logo.height}" fill="none"
                             stroke="currentColor"
                             stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                             class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24"
                             src={photo} alt={headerData.logo.src}>
                    {/await}
                {/if}
            </div>
            <nav class="md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-400	flex flex-wrap items-center text-base justify-center">
                {#each headerData.menu.links as link}
                    {#if link.dropDown == "dsaasdasd"}
                        <div class="drop-down">
                            <a href={link.href}>{link.text}</a>
                            <ul>
                                {#each link.content as subLink}
                                    <li><a href={subLink.href}>{subLink.text}</a></li>
                                {/each}
                            </ul>
                        </div>
                    {:else}
                        <a href={link.href} class = "m-5">{link.text}</a>
                    {/if}
                {/each}
            </nav>
        </div>
    </header>
{/if}
{#if headerData.menu.type === "dropdown"}
    <div class="absolute top-10 left-10 z-50">
        <div>
            <div class="dropdown relative">
                <a class=" dropdown-toggle px-12 py-5 bg-blue-600 text-white font-medium leading-tight uppercase rounded-lg shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg active:text-white transition duration-150 ease-in-out flex items-center whitespace-nowrap"
                   href="" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
                    Menu
                    <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="caret-down" class="w-2 ml-2"
                         role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
                        <path fill="currentColor"
                              d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"></path>
                    </svg>
                </a>
                <ul class=" dropdown-menu min-w-max absolute hidden bg-white text-base z-50 float-left py-2 list-none text-left rounded-lg shadow-lg mt-1 hidden m-0 bg-clip-padding border-none"
                    aria-labelledby="dropdownMenuButton2">
                    {#each headerData.menu.links as link}
                        <li>
                            <a href={link.href}
                               class=" dropdown-item py-2 px-8 font-normal block w-full whitespace-nowrap bg-transparent text-gray-700 hover:bg-gray-100">
                                {link.text}
                            </a>

                        </li>
                    {/each}
                </ul>
            </div>
        </div>
    </div>
{/if}
<style>
    /*a {*/
    /*    margin: 10px;*/
    /*}*/

    .drop-down ul {
        display: none;
        /*background-color: #9ca3af;*/
        position: absolute;
    }

    .drop-down:hover ul {
        display: block;
    }

    .drop-down ul:hover {
        display: block;
    }

</style>