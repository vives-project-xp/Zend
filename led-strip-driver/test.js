function wish(name) {
    color = "FF0000";
    console.log("Hello, "+name+"!")
    axios.get(`http://172.16.100.246/win&CL=h${color}&C2=hFFE3FF&SX=20&FX=2&A=50`).then(resp => {
    console.log(resp.data);
    });
}