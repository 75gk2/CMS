<script>
    import {Route, Router, Link} from "svelte-navigator";
    import Website from "./website/Website.svelte";
    import MainForm from "./form/MainForm.svelte";
    import NewsForm from "./form/NewsForm.svelte";

    // import * as data from './data.json'
    // console.log(data)


<<<<<<< HEAD
<main>
	<Header headerData = {data.header}/>
	<Slider sliderData = {data.content.slider}></Slider>
	<News newsData = {data.content.news}></News>
	<Footer footerData = {data.footer}>xdxd</Footer>
</main>
=======
</script>
<Router>
    <nav>
        <Link to="/">Home</Link>
        <Link to="/form">Form</Link>
    </nav>
    <Route path="/" component="{Website}"/>
    <Route path="/form" component="{MainForm}"/>
</Router>
>>>>>>> master
