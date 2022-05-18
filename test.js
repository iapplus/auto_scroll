function getElementsByXPath(xpath, parent) {
    let query = document.evaluate(xpath, parent || document,
        null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
    return query.snapshotItem(0);
}

function copy_to_clipboard(content) {
    const input = document.createElement('input');
    document.body.appendChild(input);
    input.setAttribute('value', content)
    input.select();
    if (document.execCommand('copy')) {
        console.log(document.execCommand('copy'));
    }
    document.body.removeChild(input);
}


let xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div"
let xxx = document.evaluate(xpath, document,
    null,
    XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
    null)
let x = []
for (let i = 0; i < xxx.snapshotLength; i++) {
    let href = getElementsByXPath(`/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div[${i}]//div/object/a/@href`)
    // console.log(href)
    if (href != null) {
        // x.push(href.baseURI)
        // console.log(href.nodeValue)
        if (href.nodeValue.split("?").length > 1) {
            x.push(href.nodeValue.split("?")[0])
        }
    }
}
copy_to_clipboard(x)
// console.log(x)
// console.log(Array.from(x).join(","))