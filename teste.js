const data = document.querySelector("#email")
const btnSend = document.querySelector(".send")


async function testing(email){

    details = {email: data.value}

    const response = await fetch("http://127.0.0.1:5000/auth/login", {
        method: 'POST',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(details)
    })

    const res = await response.json()

    console.log("Resultado da busca: ", res)
}

btnSend.addEventListener("click", testing)