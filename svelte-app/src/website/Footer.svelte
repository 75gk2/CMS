<script>
    // import 'tw_elements'

    export let footerData;
</script>
<footer class="bg-gray-100 text-center mt-20">
    <div class="container p-10 mx-auto border-gray-300 border-t">
        <div class="flex justify-around text-center">
            {#each footerData.links as link}
                <div>
                    <a href={link.href} class="uppercase font-bold text-gray-800">{link.text}</a>
                    {#if link.dropDown}
                        <ul class="list-none">
                            {#each link.content as subLink}
                            <li>
                                <a href={subLink.href} class="text-gray-800">{subLink.text}</a>
                            </li>
                            {/each}
                        </ul>
                    {/if}
                </div>
            {/each}
        </div>
    </div>

    <div class="text-gray-700 text-center p-4" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2022 Copyright: {footerData.companyName}
    </div>
</footer>