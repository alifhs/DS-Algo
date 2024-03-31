


// API = Application Programming Interface



// console.log("hello world");


let fruits = [
    {name: "Apple", price: 250, origin: "china"},
    {name: "Orange", price: 300, origin: "Switzerland"},
    {name: "Date", price: 1050, origin: "Saudi" }
]


let promise = new Promise((success, reject)=> {

    setTimeout(function getFruits() {
        reject(fruits);
    }, 2000)

})

promise.then((data)=> {
    console.log("fruits", data)
}).catch(e=> {
    console.log("error", e)
})