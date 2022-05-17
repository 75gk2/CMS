<script>
    import {Route, Router, Link} from "svelte-navigator";
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import NewsForm from "./form/NewsForm.svelte";

    // import * as data from './data.json'
    // console.log(data)


</script>
<Router>
    <nav>
        <Link to="/">Home</Link>
        <Link to="/form">Form</Link>
        <Link to="/form">Zaloguj</Link>
    </nav>
    <Route path="/" component="{Website}"/>
    <Route path="/form" component="{MainForm}"/>
</Router>