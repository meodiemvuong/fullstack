import React, { useEffect, useState } from 'react'
import axiosClient from '../../Api/AxiosClient'
import {Table} from 'react-bootstrap'
function UsersAdmin() {
    const [data, setData] = useState([])

    useEffect(() => {
        async function getData(){
        const url = 'http://127.0.0.1:8000/users/';
        const response = await axiosClient.get(url);
        if(response && response.data){
          setData(response.data);
        }
        }
        getData()
    }, [])

  return (
    <div>
      
        <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Gmail</th>
          </tr>
        </thead>
        <tbody>
          {
            data.map((data) => {
              return(
                <tr>
                  <td>{data.id}</td>
                  <td>{data.username}</td>
                  <td>{data.email}</td>
                </tr>
              )
            })
          }
          
          {/* <tr>
            <td>3</td>
            <td colSpan={2}>Larry the Bird</td>
            <td>@twitter</td>
          </tr> */}
        </tbody>
      </Table>
      
    </div>
  )
}

export default UsersAdmin