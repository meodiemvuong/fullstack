
import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import axiosClient from "../../Api/AxiosClient";
import './HomeAdmin.css'
function HomeAdmin(){
    const [param, setParam] = useState({
        'is_admin': false
    });
    useEffect(()=>{
        async function getData(){
        const url = 'http://127.0.0.1:8000/is_admin/'
        const response = await axiosClient.get(url);
        if(response && response.data){
            setParam(response.data)
        }
        }
        getData()
    }, [])
    
    if (!param.is_admin){
        return(
            <div className="home-admin">
                <h1>
                    Ban khong phai admin, dung co dang nhap
                </h1>
            </div>
        )
    }
    

    return(
        <div className="home-admin">
            <h1>Xin chao Admin</h1>
            <br />
            <Link to={'/admin/site/users'} >Users</Link>
        </div>
    )
}

export default HomeAdmin