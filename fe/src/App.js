import React from 'react'
import {Route, Routes} from 'react-router-dom'
import Header from './Header/Header';
import Home from './Home/Home';
import Login from './Auth/Login/Login';
import Register from './Auth/Register/Register';
import HomeAdmin from './Admin/Home/HomeAdmin';
import UsersAdmin from './Admin/Users/UsersAdmin';
import HeaderAdmin from './Admin/HeaderAdmin/HeaderAdmin';
import { BrowserRouter } from 'react-router-dom';
function App() {
  return (
    
      <BrowserRouter>
      <Routes>
        <Route path='/' element={
          <>
          <Header />
          <Home />
          </>
        } />
        <Route path="/login" element={
          <>
          <Header />
          <Login />
          </>
        } />
        <Route path="/register" element={
          <>
          <Header />
          <Register />
          </>
        } />


        <Route path="/admin/site" element={
        <>
        <HeaderAdmin />
        <HomeAdmin/>
        </>
        } />

        <Route path="/admin/site/users" element={
        <>
        <HeaderAdmin />
        <div className='users-admin' style={{
          marginLeft: '20%'
        }} >
        <UsersAdmin/>
        </div>
        </>
        } />
      </Routes>
      </BrowserRouter>
    
  );
}

export default App;
