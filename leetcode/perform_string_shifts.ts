function shiftLeft(str: String, n: Number) {
    let arr = str.split("")
    for(let i=0; i<n; i++) {
        arr.push(arr.shift())
    }
    return arr.join("")
}

function shiftRight(str: String, n: Number) {
    console.log(str, n);
    let arr = str.split("")
    for(let i=0; i<n; i++) {
        arr.unshift(arr.pop())
    }
    return arr.join("")
}

function stringShift(str: String, commands) {
    const reducer = (acc, cur) => {
        const [is_right, amount] = cur
        return (is_right ? shiftRight(acc, amount) : shiftLeft(acc, amount))
    }
    return commands.reduce(reducer, str)
}

export default stringShift
export { shiftLeft, shiftRight }
