let x = [[1,2], [[3,4]], [[[[5,6]]], 8,9] ];

let stack = [];

stack.push({"arr" : x, "cState" : 0 });

// console.log(stack.length)
while(stack.length > 0) {
    let cObj = stack.pop();
    // console.log(cObj.arr)
    for(let i = cObj.cState ; i < cObj.arr.length; i++) {
        if(Array.isArray(cObj.arr[i])) {
            stack.push({"arr" : cObj.arr, "cState": i+1});
            stack.push({"arr" : cObj.arr[i], "cState" : 0})
            // console.log("current value", cObj[i]);
            break;
        } else {
            console.log(cObj.arr[i]);
        }
    }
}

//