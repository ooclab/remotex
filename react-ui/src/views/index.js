import React from 'react'
// import { Link } from 'react-router'
import Item from 'COMPONENT/Item'
import Pagination from 'COMPONENT/Pagination'

/* 首页 布局基页 */
const IndexView = ({ children, location }) => (
  <div className="r-container">
    <Item />
    <Item />
    <Item />
    <Item />
    <Item />
    <Pagination />
  </div>
)

export default IndexView
