import {writable} from "svelte/store";

export class Login{
    static info(){
        return this.form.info
    }
    static async login(login, passwd) {
        let data = new FormData()
        data.append("login", login)
        data.append("passwd", passwd)
        let responsePromise = await fetch('http://127.0.0.1:5000/loginServiceSite', {method: "POST", body: data})
        console.log(responsePromise)
        const a = await responsePromise.json()
        console.log(a)

        let obj = {}

        if (a.status === 1000)
            obj =  {
                login: a.login,
                passwd: a.passwd,
                isAdmin: true,
                isLogged: true,
                info: "ZALOGOWANO JAKO ADMIN"
            }
        else if (a.status === 200)
            obj =  {
                login: a.login,
                passwd: a.passwd,
                isAdmin: false,
                isLogged: true,
            info: 'ZALOGOWANO JAKO '+a.login
            }
        else obj =  {
                isAdmin: false,
                isLogged: false,
                info: a.info
            }
        console.log(obj)
        return obj
    }
    static async register(login, passwd) {
        let data = new FormData()
        data.append("login", login)
        data.append("passwd", passwd)
        let res = await fetch('http://127.0.0.1:5000/registerServiceSite', {
            method: "POST",
            body: data
        })
        let json = res.json()
        return json
    }
}