document.addEventListener("readystatechange", async () => {
    if(document.readyState === "complete"){
        console.log("in the event");
    }
});
