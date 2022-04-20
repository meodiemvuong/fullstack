import React, { useEffect, useState } from 'react'
import axiosClient from '../Api/AxiosClient'
import { Link } from 'react-router-dom'
function Home() {
  const [data, setData] = useState([])

  useEffect(()=> {
    async function getData(){
      try{
        const url = 'http://127.0.0.1:8000/products/'
        const response = await axiosClient.get(url)
      // if(response && response.data){
        console.log(response)
        setData(response.data)
      // }
      }catch(err){
        console.log(err)
      }
    }
    getData();
  }, [])


  return (
    <div>
        <div className='container'>
          <div className='row'>
            {/* <div className='col-md-3'>
              Gao
            </div>
            <div className='col-md-3'>
              Gao
            </div>
            <div className='col-md-3'>
              Gao
            </div>
            <div className='col-md-3'>
              Gao
            </div> */}
            {
              data.map(data => {
                return(
                  <div className='col-md-3' key={data.id}>
                    {data.name}
                  </div>
                )
              })
            }
          </div>
        </div>
    </div>
  )
}

export default Home