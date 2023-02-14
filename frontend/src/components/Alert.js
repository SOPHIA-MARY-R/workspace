import React from "react";

export default function Alert({color, msg}){
    return(
        <div 
            style={{
                backgroundColor: color,
                color: "white",
                padding: 20,
                borderRadius: 7,
                width: "40%",
                float: "right",
                marginBottom: 10,
                marginTop: 10,
                marginRight: 10,
                opacity: 0.8
            }}
        >
            {msg}
            <span style={{color:'white', float: 'right'}}><i class="fa fa-times" aria-hidden="true"></i></span>
        </div>
    );
}