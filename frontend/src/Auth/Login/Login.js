import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import axiosClient from "../../Api/AxiosClient";
function Login(){
    const [param, setParam] = useState({
        "username": null,
        "password": null
    });
    const [message, setMessage] = useState(false)
    const navigate = useNavigate();
    console.log(param)
    const handleLogin = async()=> {
        const url = 'http://127.0.0.1:8000/login/'

        const res = await axiosClient.post(url, param);
        if(res && res.data && (res.data.Token !== undefined) ){
            localStorage.setItem('Token',res.data.Token)
            console.log(res.data)
            if(res.data.is_admin){
                navigate(`/admin/site`)
            }
            else{
                navigate('/')
            }
        }
        else{
            setMessage(true)
        }
    }
    return(
        <div>
            <div>
                <p>Username</p><input className="username" type='text' 
                onChange={(e)=>{
                    let username = e.target.value;
                    setParam({...param, "username": username})
                }}    />
                <p>Password</p><input className="password" type='password'
                onChange={(e)=>{
                    let password = e.target.value;
                    setParam({...param, "password": password})
                }}    />
                <br />
                {message && <p>Co loi xay ra, kiem tra lai thong tin</p>}
                <button onClick={()=> handleLogin()} >Đăng nhập</button>
                <br />
                <Link to={'/register'}>Đăng ký ngay</Link>
                
            </div>
            
        </div>
    )
}
export default Login