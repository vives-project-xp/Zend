const axios = require('axios');

// // CL=hC2B280&C2=hFFFFFFE&C3=hC2B280&FX=46&SX=20&A=50


    // axios.get('http://172.16.100.246/win&CL=hC2B280&C2=hFFE3FF&SX=20&FX=2&A=50').then(resp => {
    // console.log(resp.data);
    // });

function changeColor(hex_color){
    
    axios.get(`http://172.16.100.246/win&CL=h${hex_color}&C2=hFFE3FF&SX=20&FX=2&A=50`).then(resp => {
    //console.log(resp.data);
    });
    //console.log(hex_color);
}
