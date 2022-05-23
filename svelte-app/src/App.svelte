<script>
    import {Route, Router, Link} from "svelte-navigator";
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import NewsForm from "./form/NewsForm.svelte";
    import LoginForm from "./LoginForm.svelte";

    import {Login} from "./login";
    // import * as data from './data.json'
    // console.log(data)


</script>
<Router>
    <nav>
        <Link to="/">Home</Link>

        {#if Login.form.isAdmin}
            <h1>
                ZALOGOWANO JAKO ADMIN
            </h1>
        {:else }
            {#if Login.form.isAdmin}

            {:else }

                <Link to="/login">Login</Link>
            {/if}
        {/if}
    </nav>
    <Route path="/" component="{Website}"/>
    <Route path="/login" component="{LoginForm}" login={Login}/>
    <Route path="/form" component="{MainForm}"/>
</Router>

<style>
    nav{
        position: absolute;
        right:100px;
        top:70px;
    }
</style>