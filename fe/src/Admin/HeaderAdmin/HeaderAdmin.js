import React from 'react'
import './HeaderAdmin.css'
import { Link } from 'react-router-dom'

function HeaderAdmin() {
    return (
        <div className='container'>
        <div className='wrapper'>
            <div className='header'>
                
                <div className='categoryList'>
                    <div className='categoryItem'>
                        <Link className='itemLink' to="/admin/site">Admin</Link>
                        
                    </div>
                    
                </div>
            </div>
            <ul className='categoryList'>
                <li className='categoryItem'>
                    
                    <Link className='itemLink' to="/admin/site">Trang chủ</Link>
                </li>

                <li className='categoryItem'>
                    <i className="fas fa-user-friends"></i>
                    <Link className='itemLink' to="/admin/site/users">Người dùng</Link>
                </li>

                {/* <li className='categoryItem'>
                    <i className="fas fa-users"></i>
                    <Link className='itemLink' to="/admin/site/efilm">Phim bộ</Link>
                </li>
                <li className='categoryItem'>
                    <i className="fas fa-users"></i>
                    <Link className='itemLink' to="/admin/site/ffilm">Phim lẻ</Link>
                </li>
                
                <li className='categoryItem'>
                    <i className="fas fa-calendar-week"></i>
                    <Link className='itemLink' to="events">Sự kiện</Link>
                </li>
                <li className='categoryItem'>
                    <i className="fas fa-calendar-week"></i>
                    <Link className='itemLink' to="review">Góp ý</Link>
                </li> */}
            </ul>
        </div>
        </div>
      )
}

export default HeaderAdmin