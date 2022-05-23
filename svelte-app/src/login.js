export class Login{
    static form={
        login:null,
        passwd:null,
        isAdmin:false,
        isLogged:false
    }

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
                if (a.status == 1000){
                    this.form.login={
                        login:a.login,
                        passwd:a.passwd,
                        isAdmin: true,
                        isLogged: true
                    }
                }
                else if (a.status == 200){
                    this.form.login={
                        login:a.login,
                        passwd:a.passwd,
                        isAdmin: false,
                        isLogged: true
                    }
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