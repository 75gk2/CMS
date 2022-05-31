<script>
    import {Route, Router, Link} from "svelte-navigator";
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import LoginForm from "./LoginForm.svelte";

    import {Login} from "./login";
    import {writable} from "svelte/store";
    import SiteForm from "./form/SiteForm.svelte";
    import Article from "./Article.svelte";
    import Search from "./Search.svelte";

    // localStorage.removeItem("loginData")
    const loginData = writable(
        JSON.parse(localStorage.getItem("loginData")) ||
        {
            isLogged: false,
            isAdmin: "OJOJ"
        })
    loginData.subscribe(value => localStorage.setItem("loginData",JSON.stringify(value)))
    console.log(loginData)
    function resetLogin(){
        $loginData.login = ""
        $loginData.passwd = ""
        $loginData.isAdmin = false
        $loginData.isLogged = false
        $loginData.info = ""
        console.log(loginData)
    }
</script>
<Router>
    <nav class="absolute top-10 p-5 right-10 bg-gray-500 text-white rounded-lg z-50">
        <Link to="/" class="p-3">Home</Link>
        <Link to="/search" class="p-3">Search</Link>
        {#if $loginData.isLogged}
            {#if $loginData.isAdmin}
                <Link to="/form" class="p-3">Form</Link>
                <Link to="/newSite" class="p-3">Edit articles</Link>
                <Link to="/" class="p-3" on:click={resetLogin}>Log out</Link>
            {:else }
                <Link to="/" class="p-3" on:click={resetLogin}>Log out</Link>
            {/if}
        {:else }
            <Link to="/login" class="p-3">Login</Link>
        {/if}
    </nav>
    <Route path="/" component="{Website}"/>
    <Route path="/search" component="{Search}"/>
    <Route path="/login" component="{LoginForm}" loginData={loginData} login={Login}/>
    <Route path="/form" component="{MainForm}"/>
    <Route path="/newSite" component="{SiteForm}"/>
    <Route path="/article/:link" component="{Article}" loginData={loginData}/>
</Router>
