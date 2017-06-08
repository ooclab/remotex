import React from 'react'
import { Link } from 'react-router'

const Welcome = () => (
  <div className="jumbotron">
    <h1>欢迎使用 <br/> React Demo</h1>
    <p>
      <Link
        to="/msg"
        role="button"
        className="btn btn-success btn-lg">
        前往留言板 &gt;
      </Link>
      &nbsp;
      <Link
        to="/todo"
        role="button"
        className="btn btn-success btn-lg">
        前往待办事项(新功能) &gt;
      </Link>
    </p>
  </div>
)

export default Welcome
