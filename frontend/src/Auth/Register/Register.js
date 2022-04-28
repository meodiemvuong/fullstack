import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register(){
    const [param, setParam] = useState({
        "username": null,
        "email": null,
        "password": null,
        "re_password": null
    })
    console.log(param)
    const navigate = useNavigate()
    const [message, setMessage] = useState(false)
    const handleRegister = async()=>{
        const url = 'http://localhost:8000/users/'
        if(param.password !== param.re_password){
            setMessage(true);
        }
        const response = await axios.post(url, param);
        if(response && response.data){
            // console.log(response);
            navigate('/login')
        }
    }
    return(
        <div>
            <h1>Register trang nay</h1>
            <div>
                <p>Username</p><input className="username" type='text' 
                onChange={(e)=>{
                    let username = e.target.value;
                    setParam({...param, "username": username})
                }}    />
                <p>Email</p><input className="email" type='email' 
                onChange={(e)=>{
                    let email = e.target.value;
                    setParam({...param, "email": email})
                }}    />
                <p>Password</p><input className="password" type='password'
                onChange={(e)=>{
                    let password = e.target.value;
                    setParam({...param, "password": password})
                }}    />
                <p>Confirm password</p><input className="password" type='password'
                onChange={(e)=>{
                    let re_password = e.target.value;
                    setParam({...param, "re_password": re_password})
                }}    />
                {message && <p>Co loi xay ra, kiem tra lai thong tin</p>}
                <br />
                <button onClick={()=> handleRegister()} >Đăng ký</button>
                
            </div>
        </div>
    )
}

export default Register