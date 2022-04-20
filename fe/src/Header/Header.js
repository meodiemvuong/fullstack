import { Link, useNavigate } from "react-router-dom"
import axiosClient from "../Api/AxiosClient";
// import "./Header.css"
import {Nav, Container, Navbar, NavDropdown, Form, FormControl, Button} from "react-bootstrap"
function Header(){
    const token = localStorage.getItem('Token');
    const navigate = useNavigate()
    const handleLogout = async()=>{
      localStorage.removeItem('Token');
      const url = 'http://127.0.0.1:8000/logout/'
      const response = await axiosClient.post(url,{})
      console.log(response)
      navigate('/login');
    }
    return (
        <div > 
          <Navbar bg="light" expand="lg">
            <Container>
              <Link to={'/'} className='navbar-brand'>Nông sản</Link>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                <Link className="nav-link" to={'/'}>Home</Link>
                
                  {/* <Link className="nav-link" to={'/admin'}>Hello</Link> */}
                  <NavDropdown title="Tài khoản" id="basic-nav-dropdown">
                    {!token && 
                    <>
                    <Link to="/login" className='dropdown-item'>Đăng nhập</Link>
                    <Link to={'/register'} className='dropdown-item'>Đăng ký</Link>
                    </>
                    }
                    {token && 
                    <>
                    <Link to={'/information'} className='dropdown-item'>Thông tin</Link>
                    <NavDropdown.Divider />
                    <NavDropdown.Item onClick={()=> {handleLogout()}}>Đăng xuất</NavDropdown.Item></>
                    }
                  </NavDropdown>
                </Nav>
                <Form className="d-flex">
                  <FormControl
                    type="search"
                    placeholder="Search"
                    className="me-2"
                    aria-label="Search"
                  />
                  <Button variant="outline-success">Search</Button>
                </Form>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </div>
    )
}

export default Header