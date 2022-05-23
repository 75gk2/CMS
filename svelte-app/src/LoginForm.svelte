<script>
    import {writable} from "svelte/store";

    export let login;

    const loginFormValues = writable({
        login:"",
        passwd:""
    })
    const registerFormValues = writable({
        login:"",
        passwd:""
    })

</script>
{#if login.form.isLogged}
<div class = "flex justify-around w-full">
<div class="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
    <form on:submit|preventDefault={()=>login.login($loginFormValues.login, $loginFormValues.passwd)}>
        Log In
        <div class="form-group mb-6">
            <label for="exampleInputEmail2" class="form-label inline-block mb-2 text-gray-700">Login</label>
            <input bind:value={$loginFormValues.login} type="text" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleInputEmail2" placeholder="Login">
        </div>
        <div class="form-group mb-6">
            <label for="exampleInputPassword2" class="form-label inline-block mb-2 text-gray-700">Password</label>
            <input bind:value={$loginFormValues.passwd} type="password" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleInputPassword2"
                   placeholder="Password">
        </div>

        <button type="submit" class=" w-full px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Sign in</button>
    </form>
</div>

<div class="block p-6 rounded-lg shadow-lg bg-white max-w-md">
    <form on:submit|preventDefault={()=>login.register($registerFormValues.login, $registerFormValues.passwd)}>
        Register
        <div class="grid grid-cols-2 gap-4">
            <div class="form-group mb-6">
                <input bind:value={$registerFormValues.login} type="text" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleInput123"
                      aria-describedby="emailHelp123" placeholder="Login">
            </div>
        </div>
        <div class="form-group mb-6">
            <input bind:value={$registerFormValues.passwd} type="password" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="exampleInput126"
                   placeholder="Password">
        </div>
        <button type="submit" class=" w-full px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Sign up</button>
    </form>
</div></div>

{:else }
    {#if login.form.isAdmin}
        <h1>
            ZALOGOWANO JAKO ADMIN
        </h1>
    {:else }
        <h1>
            ZALOGOWANO JAKO USER
        </h1>
    {/if}
{/if}
