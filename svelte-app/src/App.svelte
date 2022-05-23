<script>
    import {Route, Router, Link} from "svelte-navigator";
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import NewsForm from "./form/NewsForm.svelte";
    import LoginForm from "./LoginForm.svelte";

    // import * as data from './data.json'
    // console.log(data)


</script>
<Router>
    <nav>
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
    </nav>
    <Route path="/" component="{Website}"/>
    <Route path="/login" component="{LoginForm}"/>
    <Route path="/form" component="{MainForm}"/>
</Router>

<style>
    nav{
        position: absolute;
        right:100px;
        top:70px;
    }
</style>