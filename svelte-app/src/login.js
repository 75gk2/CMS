import {writable} from "svelte/store";

export class Login{
    static info(){
        return this.form.info
    }
    static form=writable({
        login:null,
        passwd:null,
        isAdmin:false,
        isLogged:false,
        info:""
    })

    static login(login, passwd){
        let data = new FormData()
        data.append("login",login)
        data.append("passwd",passwd)
        let res = fetch('http://127.0.0.1:5000/loginServiceSite', {
            method: "POST",
            body: data
        })
        res.then(a=>a.json())
            .then(a=>{
                this.form.info = a.info
                if (a.status === 1000){
                        this.form.login = a.login
                        this.form.passwd = a.passwd
                        this.form.isAdmin =  true
                        this.form.isLogged =  true
                }
                else if (a.status === 200){
                    this.form.login = a.login
                    this.form.passwd = a.passwd
                    this.form.isAdmin =  false
                    this.form.isLogged =  true
                }
            })

        console.log(res)
    }
    static register(login, passwd){
        let data = new FormData()
        data.append("login",login)
        data.append("passwd",passwd)
        let res = fetch('http://127.0.0.1:5000/registerServiceSite', {
            method: "POST",
            body: data
        })
        res.then(a=>a.json())
            .then(a=>console.log(a))
    }
}