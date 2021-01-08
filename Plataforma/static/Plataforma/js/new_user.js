let passw = document.getElementById("password")
let passwA = document.getElementById("passwordA")
let form = document.getElementById("form")
let elem = document.getElementById("flag1")

window.onload = function(){
    form.addEventListener("submit", (e)=>{
        if(passw.value != passwA.value){
            if(!document.getElementById("aviso")){
                let aviso = document.createElement("p")
                aviso.id = "aviso"
                aviso.classList.add("alert")
                aviso.classList.add("alert-danger")
                let texto = document.createTextNode("Las contraseñas no coinciden")
                aviso.appendChild(texto)
                form.insertBefore(aviso, elem)
            }
            e.preventDefault()
        }
    })
    passw.addEventListener("focus", ()=>{
        if(document.getElementById("aviso")){
            form.removeChild(aviso)
        }
    })
}

