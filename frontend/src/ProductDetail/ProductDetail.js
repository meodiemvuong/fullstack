import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axiosClient from '../Api/AxiosClient';

function ProductDetail() {
    const {id} = useParams();
    const [data, setData] = useState({});
    useEffect(()=>{
        async function getData() {
            const response = await axiosClient.get(`products/${id}`);
            if(response && response.data){
                setData(response.data)
            }
        }
        getData();
    }, [])
    console.log(data);
  return (
    <div>ProductDetail</div>
  )
}

export default ProductDetail