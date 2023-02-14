import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import Alert from "./Alert";

const url = "http://127.0.0.1:8000/api";

export default function Dropzone(){
    //state for displaying alert
    const [alert, setAlert]=useState({
        isVisible: false,
        type: null,
        msg: null,
    })
    //dropzone setup
    const onDrop=(img_file)=>{
        setAlert({
            isVisible: false,
            type: null,
            msg: null,
        })
        sendImage(img_file)
    }
    const {getRootProps, getInputProps, isDragActive}=useDropzone({
        onDrop,
        multiple: false,
    })
    
    //send image
    const sendImage=async(image)=>{
        try{
            let formData=new FormData()
            formData.append('pic', image[0], image[0].name)
            const response=await fetch(`${url}/images/`,{
                method: 'POST',
                body: formData
            })
            const data=await response.json()
            const {id}=data
            getImage(id)
        }
        catch(e){
            console.log(e)
            setAlert({isVisible:true, type:'error', msg:'Oops..something went wrong!!'})
        }
    }
    // get image
    const getImage=async(id)=>{
        try{
            const response=await fetch(`${url}/images/${id}/download/`, {
                method: 'GET',
                responseType: 'blob',
            });
            const  data=await response.blob()
            const href=window.URL.createObjectURL(data)
            const downloadLink=document.createElement('a')
            downloadLink.href=href
            downloadLink.setAttribute('download', 'removed_bg_pic.png')
            document.body.appendChild(downloadLink)
            downloadLink.click()
            document.body.removeChild(downloadLink)  
            setAlert({isVisible:true, type:'success', msg:'Download successfull!'})          
        }   
        catch (e){
            console.log(e) 
            setAlert({isVisible:true, type:'error', msg:'Oops..something went wrong!!'})
        }
    }

    const {isVisible, type, msg} = alert;
    return (
        <div>
            {isVisible && <Alert color={type==='success' ? 'green' : 'red'} msg={msg}/>}
            <br/>
            <div {...getRootProps({ className:"dropZone" })}>
                <input {...getInputProps}/>
                <p>
                    {isDragActive
                        ? "Drop an image"
                        : "Drag & Drop image to remove background"
                    }
                </p>
            </div>
        </div>
    );
}