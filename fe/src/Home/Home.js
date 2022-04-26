import React, { useEffect, useState } from 'react'
import axiosClient from '../Api/AxiosClient'
import { Link } from 'react-router-dom'
import './Home.css'
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
            
            {
              data.map(data => {
                return(
                  <div className='col-md-3'>
                    
                    <div class="card">
                    <img class="card-img-top" src={data.image} alt="Card image cap"/>
                    <div class="card-body">
                      <Link to={`/products/${data.id}`}>
                      <h5 class="card-title">{data.name}</h5>
                      </Link>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
                    </div>
                  // <div className='col-md-3' key={data.id}>
                  //   <div >
                  //   <img className='image-card' src={data.image} />
                  //   </div>
                  //   {data.name}
                  // </div>
                )
              })
            }
            
          </div>
        </div>
    </div>
  )
}

export default Home